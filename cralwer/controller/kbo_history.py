from os import getcwd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd


# url ='https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9'
# driver = webdriver.Chrome('chromedriver')
# driver.maximize_window()

# driver.get(url)
# html = BeautifulSoup(driver.page_source,'lxml')


# ### 야구다 야구!!!!!!!!
# month_list =['04','05','06','07','08','09','10']
# dates =[]
# win =[]
# lose =[]
# places =[]

# for k in range(2001,2022):
#     driver.find_element(By.XPATH, '//*[@id="ddlYear"]').send_keys(str(k))
#     for j in month_list:
#         driver.find_element(By.XPATH, '//*[@id="ddlMonth"]').send_keys(j)
#         # elem = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'#tblSchedule > tbody > tr')))        
#         elem = BeautifulSoup(driver.page_source,'lxml').find('tbody')
#         driver.implicitly_wait(1)

#         date = elem.find_all("td", {"class": "day"})
#         play = elem.find_all("td", {"class": "play"})
#         trs = elem.find_all("tr")

#         for i in range(len(play)):
            
#             if len(play[i].text.split('vs')[0]) <3 or len(play[i].text.split('vs')[1]) <3:
#                 continue
                
#             team1 = int(re.findall(r'\d+',play[i].text.split('vs')[0])[0])
#             team2 = int(re.findall(r'\d+',play[i].text.split('vs')[1])[0])
#             # print(team1,team2)
#             t1 = play[i].text.split('vs')[0]
#             t1 = ''.join([i for i in t1 if not i.isdigit()])

#             t2 = play[i].text.split('vs')[1]
#             t2 = ''.join([i for i in t2 if not i.isdigit()])
#             # print(t1,t2)


#             if team1>team2 :
#                 win.append(t1)
#                 lose.append(t2)
#             else:
#                 win.append(t2)
#                 lose.append(t1)
#             place = trs[i].find_all("td")[-2].text
#             places.append(place)
    


# data = []

# for i in range(len(win)):
#     data.append({"win" : win[i] ,"lose" :lose[i] , "place":places[i]})
    
# print(len(data))

# data_set = pd.DataFrame(data)
# data_set.to_csv("./kbo_history.csv", index = False, encoding = 'cp949')

def winning_rate(team1, team2):
    
    url ='https://www.koreabaseball.com/Schedule/Schedule.aspx?seriesId=0,9'
    driver = webdriver.Chrome('C:\\Users\\kdh\\Desktop\\pythonProjects\\project_mini_web_crawling\\crawler_project\\cralwer\\controller\\chromedriver.exe')
    driver.maximize_window()

    driver.get(url)
    html = BeautifulSoup(driver.page_source,'lxml')


    ### 야구다 야구!!!!!!!!
    month_list =['04','05','06','07','08','09','10']
    dates =[]
    win =[]
    lose =[]
    places =[]

    for k in range(2001,2022):
        driver.find_element(By.XPATH, '//*[@id="ddlYear"]').send_keys(str(k))
        for j in month_list:
            driver.find_element(By.XPATH, '//*[@id="ddlMonth"]').send_keys(j)
            # elem = WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,'#tblSchedule > tbody > tr')))        
            elem = BeautifulSoup(driver.page_source,'lxml').find('tbody')
            driver.implicitly_wait(1)

            date = elem.find_all("td", {"class": "day"})
            play = elem.find_all("td", {"class": "play"})
            trs = elem.find_all("tr")

            for i in range(len(play)):
                
                if len(play[i].text.split('vs')[0]) <3 or len(play[i].text.split('vs')[1]) <3:
                    continue
                    
                team1 = int(re.findall(r'\d+',play[i].text.split('vs')[0])[0])
                team2 = int(re.findall(r'\d+',play[i].text.split('vs')[1])[0])
                # print(team1,team2)
                t1 = play[i].text.split('vs')[0]
                t1 = ''.join([i for i in t1 if not i.isdigit()])

                t2 = play[i].text.split('vs')[1]
                t2 = ''.join([i for i in t2 if not i.isdigit()])
                # print(t1,t2)


                if team1>team2 :
                    win.append(t1)
                    lose.append(t2)
                else:
                    win.append(t2)
                    lose.append(t1)
                place = trs[i].find_all("td")[-2].text
                places.append(place)
        


    data = []

    for i in range(len(win)):
        data.append({"win" : win[i] ,"lose" :lose[i] , "place":places[i]})
        
    print(len(data))

    data_set = pd.DataFrame(data)
    data_set.to_csv("./kbo_history.csv", index = False, encoding = 'cp949')

    condition = ((data_set.win == team1) & (data_set.lose == team2)) | ((data_set.win == team2) & (data_set.lose == team1))
    df = data_set[condition]
    total = len(df)
    win=len(df[df.win ==team1])
    print("%s와(과) %s의 경기에서 %s의 승률은 : %.2f%%" %(team1, team2, team1, win/total * 100))
