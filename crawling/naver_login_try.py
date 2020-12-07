from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
# webdriver.Chrome에 다운받은 chromedriver 경로
# userId, userPwds에 아이디, 비번


##### 네이버 자동방지 시스템 작동으로 되지 않는다.

# driver = webdriver.Chrome("경로")
driver = webdriver.Chrome("C:/Users/bulge/Documents/Python Scripts/Kakao_Chatbot_Project/PCchatbot/chromedriver.exe")
delay_time = 3
driver.implicitly_wait(delay_time)

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

# userId = "아이디"
# userPwd = "비밀번호"
userId = "bulgen"
userPwd = "mayplen0522"
id_list = list(userId)
pw_list = list(userPwd)
for i in range(len(id_list)):
    driver.find_element_by_name('id').send_keys(id_list[i])
    sleep(1)
for j in range(len(pw_list)):
    driver.find_element_by_name('pw').send_keys(pw_list[j])
    sleep(1)


# driver.find_element_by_name('id').send_keys(userId)
# driver.find_element_by_name('pw').send_keys(userPwd)

# # 로그인을 누를 수 있다.
# driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/form/fieldset/input').click()

# driver.get("http://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=10573&searchWord=&_csrf=67b81ea4-b54a-4340-bcc4-366b330434de&pageIndex=1")

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# data = soup.find('a', class_='onair')['href']
# print("강의 링크는,",data,"야. \n오늘도 수업 열심히 듣자:)")

# driver.close()
