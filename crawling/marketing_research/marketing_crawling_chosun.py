# -*- coding: utf-8 -*-
import pandas as pd
import requests, bs4
import re
import time
from selenium import webdriver
from datetime import datetime
import json
from konlpy.tag import Okt

#---------------------------------------------------------------------------------------
okt=Okt()
#---------------------------------------------------------------------------------------
# 이건 군산대 감성어사전에 데이터 집어넣기 위한 class 인 듯!
class KnuSL():
    def data_list(wordname):
        with open('data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
            data = json.load(f)
        result = ['None', 'None']
        for i in range(0, len(data)):
            if data[i]['word'] == wordname:
                result.pop()
                result.pop()
                result.append(data[i]['word_root'])
                result.append(data[i]['polarity'])
        r_word = result[0]
        s_word = result[1]
        return r_word, s_word
ksl = KnuSL
#---------------------------------------------------------------------------------------

open_main_url = ('https://www.chosun.com/')
main_resp = requests.get(open_main_url)
#print(main_resp.encoding)
main_resp.encoding='utf-8'
#main_resp.encoding=None
main_bs = bs4.BeautifulSoup(main_resp.text, 'html.parser')
elements = main_bs.find_all('dl', 'news_item')

p = re.compile('^https://news.chosun.com/')

# by BeautifulSoup
article_urls = []

article_types = [] #news

article_location_1 = []
article_location_2 = []

article_onclick_others = []

# by selenium

article_titles = []
article_reporter = []

article_time_access = []
article_time_uploaded_reviesed = []

article_sections = [] #정치 일반

article_num_facebook_share = []
article_num_comments = []
article_num_likes = []

article_contents = []
article_num_good_words = []
article_num_bad_words = []
article_num_neutral_words = []
article_num_none_words = []

article_num_all_words = []
article_num_long_words = []

for element in elements:
    if p.match(element.find('a')['href']):
        try:
            article_urls.append(element.find('a')['href'])
            article_location_1.append(element.find('a')['onclick'].replace("ga(\'","").replace(');',"").replace("\'","").replace(" ","").split(',')[2])
            article_location_2.append(element.find('a')['onclick'].replace("ga(\'","").replace(');',"").replace("\'","").replace(" ","").split(',')[4])

            article_types.append(element.find('a')['onclick'].replace("ga(\'","").replace(');',"").replace("\'","").replace(" ","").split(',')[3])
            article_onclick_others.append(element.find('a')['onclick'].replace("ga(\'","").replace(');',"").replace("\'","").replace(" ","").split(',')[0:2])
            print('Crawled article')
        except:
            print('Not an article')
            print('--------------------------')
print(article_urls)

driver = webdriver.Chrome('C:/Users/user/Downloads/chromedriver_win32/chromedriver')
for article_url in article_urls:
    driver.implicitly_wait(5)
    driver.get(article_url)
    time.sleep(5)
    #-----------------------------------------------------------------
    words = okt.morphs(driver.find_element_by_css_selector('#news_body_id > div.par').text)
    article_contents.append(driver.find_element_by_css_selector('#news_body_id > div.par').text.split())
    tmp_good=0
    tmp_bad=0
    tmp_neutral=0
    tmp_none=0
    tmp_long_word=0

    for word in words:
        if len(word)>=3:
            tmp_long_word += 1

        if ksl.data_list(word)[1] == 'None':
            tmp_none += 1
        else:
            sentiment = int(ksl.data_list(word)[1])
            if sentiment > 0:
                tmp_good += 1
            elif sentiment < 0:
                tmp_bad += 1
            else:
                tmp_neutral += 1

    article_num_good_words.append(tmp_good)
    article_num_bad_words.append(tmp_bad)
    article_num_neutral_words.append(tmp_neutral)
    article_num_none_words.append(tmp_none)

    article_num_all_words.append(len(words))
    article_num_long_words.append(tmp_long_word)
    #-----------------------------------------------------------------

    article_titles.append(driver.find_element_by_css_selector('#news_title_text_id').text)
    article_reporter.append(driver.find_element_by_css_selector('#csContent > header > div > div > ul > li > a').text)

    article_time_access.append(datetime.today().strftime("%Y.%m.%d %H:%M"))
    article_time_uploaded_reviesed.append(driver.find_element_by_css_selector('#news_body_id > div.news_date').text)

    article_sections.append(driver.find_element_by_css_selector('#news_cat_trig_id').text)

    article_num_facebook_share.append(driver.find_element_by_css_selector('#news_left_aside_id > ul > li:nth-child(3) > a > span').text)
    article_num_comments.append(driver.find_element_by_css_selector('#BBSCNT').text)
    article_num_likes.append(driver.find_element_by_css_selector('#CSCNT').text)

df_chosun = pd.DataFrame()

df_chosun['article_titles']=article_titles
df_chosun['article_urls']=article_urls

df_chosun['article_time_access']=article_time_access
df_chosun['article_time_uploaded_reviesed']=article_time_uploaded_reviesed

df_chosun['article_types']=article_types
df_chosun['article_sections']=article_sections
df_chosun['article_location_1']=article_location_1
df_chosun['article_location_2']=article_location_2

df_chosun['article_num_facebook_share']=article_num_facebook_share
df_chosun['article_num_comments']=article_num_comments
df_chosun['article_num_likes']=article_num_likes

df_chosun['article_contents']=article_contents
df_chosun['article_num_good_words']=article_num_good_words
df_chosun['article_num_bad_words']=article_num_bad_words
df_chosun['article_num_neutral_words']=article_num_neutral_words
df_chosun['article_num_none_words']=article_num_none_words

df_chosun['article_reporter']=article_reporter
df_chosun['article_onclick_others']=article_onclick_others

df_chosun.to_csv('chosun_{}'.format(datetime.today().strftime("%Y%m%d_%H-%M")))