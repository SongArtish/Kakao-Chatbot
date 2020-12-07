import requests, bs4
import time
from urllib.parse import quote
from datetime import datetime
from selenium import webdriver

article_urls = []

good_lists = []
warm_lists = []
sad_lists = []
angry_lists = []
want_lists = []

comment_num_lists = []
comment_num_delete_lists = []
comment_num_violate_lists = []

sort_lists=[]

open_main_url = ('https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=023&listType=title&date={}'.format(datetime.today().strftime("%Y%m%d")))
main_resp = requests.get(open_main_url)
main_bs = bs4.BeautifulSoup(main_resp.text, 'html.parser')
page_urls = main_bs.find_all('div', 'paging','a')
last_page = int(str(page_urls).split('</a>')[-2][-1])

url_lists = []
for page in range(1,(last_page+1)):
    print('page {} crawling'.format(page))

    open_page_url = ('https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&oid=023&listType=title&date={}&page={}'.format(datetime.today().strftime("%Y%m%d"),page))
    page_resp = requests.get(open_page_url)
    page_bs = bs4.BeautifulSoup(page_resp.text, 'html.parser')
    url_groups = main_bs.find_all('ul', 'type02')
    for url_group in url_groups:
        urls = url_group.find_all('li')
        for url in urls:
            url_lists.append(url.find('a')['href'])
    time.sleep(5)(

driver = webdriver.Chrome'C:/Users/user/Downloads/chromedriver_win32/chromedriver')
for url in url_lists:
    driver.implicitly_wait(5)
    driver.get(url)
    time.sleep(5)

    good_lists.append(driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.good > a > span.u_likeit_list_count._count').text)
    warm_lists.append(driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.warm > a > span.u_likeit_list_count._count').text)
    sad_lists.append(driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.sad > a > span.u_likeit_list_count._count').text)
    angry_lists.append(driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.angry > a > span.u_likeit_list_count._count').text)
    want_lists.append(driver.find_element_by_css_selector('#spiLayer > div._reactionModule.u_likeit > ul > li.u_likeit_list.want > a > span.u_likeit_list_count._count').text)

    comment_num_lists.append(driver.find_element_by_css_selector('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_new > div.u_cbox_comment_count_wrap > ul > li:nth-child(1) > span').text)
    comment_num_delete_lists.append(driver.find_element_by_css_selector('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_new > div.u_cbox_comment_count_wrap > ul > li:nth-child(2) > span').text)
    comment_num_violate_lists.append(driver.find_element_by_css_selector('#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_new > div.u_cbox_comment_count_wrap > ul > li:nth-child(3) > span').text)

    tmp_sort_lists=[]
    for a in driver.find_elements_by_css_selector('.u_cbox_sort_label'):
        tmp_sort_lists.append(a.text)

    sort_lists.append(tmp_sort_lists)
    print('Crawled article')