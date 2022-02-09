import matplotlib.pyplot as plt
import requests
import pandas as pd
from django.utils.timezone import localtime
from typing import Optional
from cralwer.const import corona_api_key,base_url_country,base_url_vaccine,REGION_NAME
from cralwer.common import set_plt

# API
# https://github.com/dhlife09/Corona-19-API


# COMMON

def get_dataframe_from_country_api(base_url:str,api_key:str):
    res = requests.get(''.join([base_url,api_key])).json()

    if res['resultCode'] == 200 or res['resultCode'] == '0':
        print('API 요청 성공')
        
        res.pop('resultCode')
        res.pop('resultMessage')
        
        return pd.DataFrame(res)
    else:
        print('API 요청 실패')
        print(res['resultCode'])
        exit(1)

# COMMON

def get_dataframe_from_vaccine_api(base_url:str,api_key:str):
    res = requests.get(''.join([base_url,api_key])).json()
    status = res['API']
    
    if status['resultCode'] == '200':
        print('API 요청 성공')
        
        res.pop('API')
        return pd.DataFrame(res)
    else:
        print('API 요청 실패')
        print(status['resultCode'])
        exit(1)

# 백신 접종 현황
# tag : [ '지역명' 또는 '전체' ]
# 지역명 : ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

def corona_data_vaccine(df:pd.DataFrame,tag:str = '전체'):
    if df is None or tag not in REGION_NAME:
        return {'message':'ERROR'}
    
    copied:Optional[pd.DataFrame] = df.copy()
    copied.drop('countryNm',axis=0,inplace=True)
    copied.columns = REGION_NAME
    
    if tag == '전체':
        copied = df['korea'].copy().to_dict()
        copied['countryNm'] = '전체'
    else:
        copied = df[tag].copy().to_dict()
    
    vaccine_keys = ['접종_완료_전체','신규_접종_완료','기존_접종_완료']
    
    res = {}
    for k,v in copied.items():
        if k == 'countryNm':
            res['지역명'] = v
        else:
            new_key = '{}차_접종'.format(k.split('_')[-1])
            new_val = {}
            original_value = list(v.values())
            print(original_value)
            for i in range(len(vaccine_keys)):
                new_val[vaccine_keys[i]] = original_value[i]
                
            res[new_key] = new_val
    
    return res

# COUNTRY
# 시도별 발생동향
# tag : ['지역명' 또는 '전체']
# 지역명 : ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
def corona_data_country(df:pd.DataFrame,tag:str = '전체',chart:bool=False):
    if df is None or tag not in REGION_NAME:
        return {'message':'ERROR'}

    copied = df.copy()
    # preprocessing
    copied.drop(['countryName','percentage'],axis=0,inplace=True)
    copied.drop(['quarantine'],axis=1,inplace=True)
    
    copied.columns = REGION_NAME
    kor_index = ['신규확진환자수','확진환자수','완치자수','사망자','전일대비증감-해외유입','전일대비증감-지역발생']
    copied.index = kor_index
    
    for i in copied.columns.tolist():
        copied[i] = pd.to_numeric(copied[i].map(lambda x : x.replace(',','') ))
    
    # draw chart or send dict
    
    if chart:
        if tag == '전체':
            copied.drop(['korea'],axis=1,inplace=True)
            copied.plot(kind='bar',figsize=(15,8),legend=True)
        else:
            copied[tag].plot(kind='bar',figsize=(15,8),legend=True)
        
        file_name = f'{localtime().__str__()}.png'
        plt.savefig(f'./{file_name}')
        
        return file_name    
    else:
        if tag == '전체':
            return copied['korea'].to_dict()
        else:
            return copied[tag].to_dict()

def corona_api(queries=None):
    set_plt()
    
    df_country = get_dataframe_from_country_api(base_url_country,corona_api_key)
    corona_data_country(df_country,'대구',chart=False)

    df_vaccine = get_dataframe_from_vaccine_api(base_url_vaccine,corona_api_key)
    corona_data_vaccine(df_vaccine)
    
    return {'message':'받아라 나의 딕셔너리'}

