from selenium import webdriver
from bs4 import BeautifulSoup
import requests


base_url = 'https://sports.naver.com'
driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()


driver.get(base_url)
html = BeautifulSoup(driver.page_source,'lxml')
tags = html.find('div',{'id':'_sports_lnb_menu'})

lis = tags.find_all('li', {'class': "main_menu_item"})
links =[]
banner_list =['스포츠홈','야구','해외야구','축구','해외축구','농구','배구']

for li in lis:
    a= li.find("a", {"class":"link_main_menu"})
    links.append(base_url + a['href'])


#국내야구 결과 출력
def kbaseball(html):
    tag= html.find("div", {"id":"calendarWrap"})
    divs = tag.find_all("tbody")

    for div in divs:
        date = div.find("strong")
        if date == -1 or date == None:
            continue
      

        
        team_left = div.find_all("span",{"class":"team_lft"})
        team_right = div.find_all("span", {"class": "team_rgt"})
        


        if team_left == []:
            continue
        if team_right == []:
            continue
        
        print(date.text)
        left =[]
        right = []
        
        for j in team_left :
            left.append(j.text)
        for j in team_right:
            right.append(j.text)
        for i in range(len(left)):
            print(left[i], 'vs',right[i])
        


#해외야구 결과 출력 
def wbaseball(html):
    tag = html.find(("tbody", {"id" : "_monthlyScheduleList"}))
    trs = tag.find_all("tr")
# for tr in trs:
#     print(tr.text)
    for i in range(len(trs)):
    
        date = trs[i].find('th',{"rowspan":"1"})
        if date ==None:
            continue
        date = date.find("div", {"class": "inner"})
        result = trs[i].find_all('span')

        print(date.text)
        team_left = result[3]
        left_result = result[4]
        team_right = result[7]
        right_result = result[8]

        print("%s %s : %s %s"%(team_left.text,left_result.text,right_result.text,team_right.text))


#축구 일정/결과 
def ksoccer(html):
    tag = html.find("tbody", {"id": "_monthlyScheduleList"})
    trs = tag.find_all("tr")

    a =None
    for tr in trs:
        date = tr.find("em")
        if date != None:
            a=date
        else:
            date = a
        spans = tr.find_all("span")
        if spans[0].text =="경기가 없습니다.":
            continue
            print(date.text ,spans[0].text)
        elif len(spans)==9:
            print("%s %s %s:%s %s"%(date.text , spans[3].text, spans[4].text, spans[7].text ,spans[6].text))
        else:
            print("%s %s vs %s"%(date.text , spans[3].text, spans[5].text))
        
        
  
  #해외축구 일정/결과 
def wsoccer(html):
    tag = html.find("tbody", {"id": "_monthlyScheduleList"})
    trs = tag.find_all("tr")

    a =None
    for tr in trs:
        date = tr.find("em")
        if date != None:
            a=date
        else:
            date = a
        spans = tr.find_all("span")
        if spans[0].text =="경기가 없습니다.":
            continue
            print(date.text ,spans[0].text)
        elif len(spans)==9:
            print("%s %s %s:%s %s"%(date.text , spans[3].text, spans[4].text, spans[7].text ,spans[6].text))
        else:
            print("%s %s vs %s"%(date.text , spans[3].text, spans[5].text))
        
        
  
  #농구
def basketball(html):
    tag = html.find("div", {"class": ["sch_volleyball","tb_kbl"]})
    tbodys = tag.find_all("tbody")
    for tbody in tbodys:
        date = tbody.find("strong")
        lefts = tbody.find_all("span", {"class": "team_lft"})
        righs = tbody.find_all("span", {"class": "team_rgt"})
        score = tbody.find_all("strong", {"class": "td_score"})
        for i in range(len(lefts)):
            print("%s %s %s %s"%(date.text, lefts[i].text, score[i].text, righs[i].text))


  
        
  
#배구
def volleyball(html):
    tag = html.find("div", {"class": ["sch_volleyball","tb_kbl"]})
    tbodys = tag.find_all("tbody")
    for tbody in tbodys:
        date = tbody.find("strong")
        lefts = tbody.find_all("span", {"class": "team_lft"})
        righs = tbody.find_all("span", {"class": "team_rgt"})
        score = tbody.find_all("strong", {"class": "td_score"})
        for i in range(len(lefts)):
            print("%s %s %s %s"%(date.text, lefts[i].text, score[i].text, righs[i].text))


  
function_list=['',kbaseball,wbaseball,ksoccer,wsoccer,basketball, volleyball]


def get_url(sport):
    num = banner_list.index(sport)
    url = links[num]
    driver.get(url)
    html = BeautifulSoup(driver.page_source, 'lxml')
    lis = html.find_all("li",{"class": "sub_menu_item"})
    a= lis[3].find("a")
    final_link = url.replace('/index','')+'/schedule/index'
    driver.get(final_link)
    
    html = BeautifulSoup(driver.page_source, 'lxml')
    #kbaseball(html)
    function_list[num](html)


#banner_list =['야구','해외야구','축구','해외축구','농구','배구']

get_url("농구")