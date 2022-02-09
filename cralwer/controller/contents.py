import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def naverwebtoon(week):
    wt_url = 'https://comic.naver.com/webtoon/weekday.nhn'
    response = requests.get(wt_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw_title_list = soup.select('a.title')  
    title_list = []
    i= 1
    for a in raw_title_list:         
        a_href = a.get('href')[-3:] 
        a_text = a.get_text()   
        if a_href == week:       
            result = f'{i:2d}위 {a_text}'
            title_list.append(result)
            i+=1
            if i > 5 :
                return title_list


def n2(week):
    weeklist = ['mon','tue','wed','thu','fri','sat','sun']
    weeklist2 = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    naver_webtoon_list =[]
    for i in weeklist:
        naver_webtoon_list.append(naverwebtoon(i))
    
    for i in range(len(weeklist2)):
        if week == weeklist2[i]:
            return(naver_webtoon_list[i])

def genderwebtoon(gender,week):
    url = 'https://m.comic.naver.com/webtoon/weekday?sort='+gender+'_READER&week='+week
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_list = []
    author_list = []
    title = soup.select('ul li strong')
    author = soup.select('ul li span.author')
    
    for r in title: 
        title_list.append(r.text.strip())
    for r in author: 
        author_list.append(r.text.strip())  
    return title_list, author_list
def naver_webtoon_male(week):
    weeklist = ['mon','tue','wed','thu','fri','sat','sun']
    naver_webtoon_malelist =[]
    for i in weeklist:
        title_list, author_list = genderwebtoon('MALE',i)
        a = []
        for j in range(0, 10):
            a.append(str(j+1)+'위  ' + title_list[j]+'  |  '+author_list[j])
        naver_webtoon_malelist.append(a)
    weeklist2 = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    for i in range(len(weeklist2)):
        if week == weeklist2[i]:
            return(naver_webtoon_malelist[i])

def naver_webtoon_female(week):
    weeklist = ['mon','tue','wed','thu','fri','sat','sun']
    naver_webtoon_femalelist =[]
    for i in weeklist:
        title_list, author_list = genderwebtoon('FEMALE',i)
        a = []
        for j in range(0, 10):
            a.append(str(j+1)+'위  ' + title_list[j]+'  |  '+author_list[j])
        naver_webtoon_femalelist.append(a)
    weeklist2 = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    for i in range(len(weeklist2)):
        if week == weeklist2[i]:
            return(naver_webtoon_femalelist[i])


def get_melon_chart():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    URL='https://www.melon.com/chart/week/index.htm'
    html = requests.get(URL, headers = header)
    soup = BeautifulSoup(html.text, 'html.parser')
    titles = soup.find_all("div", {"class": "ellipsis rank01"})
    singers = soup.find_all("div", {"class": "ellipsis rank02"})
    rank = []
    title = []
    singer = []
    melon_chart = []
    for i in range(0, 100):
        rank.append(str(i+1))

    for t in titles:
        title.append(t.text.strip())

    for s in singers:
        singer.append(s.find('a').text.strip())

    for i in range(0, 10):
       melon_chart.append(rank[i]+'위  ' + title[i]+'  |  '+singer[i])

    return melon_chart


def bugs_chart():
    data = requests.get('https://music.bugs.co.kr/chart')
    soup = BeautifulSoup(data.text, 'html.parser')
    rank_lists = soup.select('.list > tbody > tr')
    b = []
    count = 0
    for rank_list in rank_lists:
        ranking = rank_list.select_one('td > div.ranking > strong').text
        m_title = rank_list.select_one('th > .title > a').text
        m_artist = rank_list.select_one('td.left > .artist > a').text
        b.append(ranking+'위  '+ m_title+'  |  '+m_artist)
        count +=1
        if count > 9:
            return b


def book_20():
    driver = webdriver.Chrome('C:\\Users\\kdh\\Desktop\\pythonProjects\\project_mini_web_crawling\\crawler_project\\cralwer\\controller\\chromedriver.exe')
    driver.get('https://mbook.interpark.com/shop/ranking/age')
    time.sleep(2)
    driver.maximize_window()
    book_20 = []
    driver.find_element(By.XPATH, '//*[@id="selectAge"]').send_keys('20')
    book_title = driver.find_elements(By.CLASS_NAME, 'multiTxtEllipsis')
    book_author = driver.find_elements(By.CLASS_NAME, 'pt5')
    title = []
    author =[]
    for elem in book_title:
        title.append(elem.text.strip())
    for elem in book_author:
        author.append(elem.text.strip())
    for i in range(len(title)):
        book_20.append(str(i+1)+'위  '+title[i]+'  |  '+author[i])
    return book_20

def book_30():
    driver = webdriver.Chrome('C:\\Users\\kdh\\Desktop\\pythonProjects\\project_mini_web_crawling\\crawler_project\\cralwer\\controller\\chromedriver.exe')
    driver.get('https://mbook.interpark.com/shop/ranking/age')
    time.sleep(2)
    driver.maximize_window()
    book_30 = []
    driver.find_element(By.XPATH, '//*[@id="selectAge"]').send_keys('30')
    time.sleep(2)
    book_title = driver.find_elements(By.CLASS_NAME, 'multiTxtEllipsis')
    book_author = driver.find_elements(By.CLASS_NAME, 'pt5')
    title = []
    author =[]
    for elem in book_title:
        title.append(elem.text.strip())
    for elem in book_author:
        author.append(elem.text.strip())
    for i in range(len(title)):
        book_30.append(str(i+1)+'위  '+title[i]+'  |  '+author[i])
    return book_30


def googledaily():
    driver = webdriver.Chrome('C:\\Users\\kdh\\Desktop\\pythonProjects\\project_mini_web_crawling\\crawler_project\\cralwer\\controller\\chromedriver.exe')
    driver.get('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR')
    time.sleep(2)
    # elem = driver.find_element(By.CLASS_NAME,'rotate-down')
    # elem.click()
    searchword = []
    views= []
    text = []
    link = []
    total = []
    a = driver.find_elements(By.CLASS_NAME,'md-list-block')
    for i in a:
        b = i.find_element(By.TAG_NAME,'a')
        searchword.append(b.text)

    a = driver.find_elements(By.CLASS_NAME,'summary-text')
    for i in a:
        b = i.find_element(By.TAG_NAME,'a')
        text.append(b.text)
        link.append(b.get_attribute("href"))
    a = driver.find_elements(By.CLASS_NAME,'search-count-title')
    for i in a:
        views.append(i.text)
    for i in range(20):
        total.append(str(i+1)+'위 검색어 : '+searchword[i])
        # total.append(str(i+1)+'위 검색어 : '+searchword[i] + '  조회수 : '+views[i] + '  관련 뉴스 : '+text[i]+'  링크 : '+link[i])
    return total


def news(rank):
    driver = webdriver.Chrome('C:\\Users\\kdh\\Desktop\\pythonProjects\\project_mini_web_crawling\\crawler_project\\cralwer\\controller\\chromedriver.exe')
    driver.get('https://trends.google.co.kr/trends/trendingsearches/daily?geo=KR')
    time.sleep(2)
    driver.fullscreen_window()
    text2 = []
    link2 = []
    a = driver.find_elements(By.CLASS_NAME,("feed-item-header"))
    for i in a:
        i.send_keys(Keys.ENTER)
        time.sleep(1)
        b = driver.find_elements(By.CLASS_NAME,'carousel-wrapper')
        for i in b:
            c = i.find_elements(By.TAG_NAME,'a')
            text = []
            link = []
            for i in c:
                text.append(i.get_attribute("title"))
                link.append(i.get_attribute("href"))
        text2.append(text)
        link2.append(link)

    for i in range(len(text2)):
        if i == rank:
            return(text2[i]+link2[i])