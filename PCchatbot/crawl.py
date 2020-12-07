from selenium import webdriver
from bs4 import BeautifulSoup
# from SECURITY import SSAFY_ID, SSAFY_PW
# webdriver.Chrome에 다운받은 chromedriver 경로
# userId, userPwds에 아이디, 비번

def youtube_link():    
    # driver = webdriver.Chrome("경로")
    driver = webdriver.Chrome("chromedriver.exe")
    delay_time = 3
    driver.implicitly_wait(delay_time)

    driver.get('https://edu.ssafy.com')

    userId = "아이디"
    userPwd = "비밀번호"
    # userId = SSAFY_ID()
    # userPwd = SSAFY_PW()
    driver.find_element_by_name('userId').send_keys(userId)
    driver.find_element_by_name('userPwd').send_keys(userPwd)

    # 로그인을 누를 수 있다.
    driver.find_element_by_xpath('//*[@id="wrap"]/div/div/div[2]/form/div/div[2]/div[3]/a').click()

    driver.get("http://edu.ssafy.com/edu/board/notice/detail.do?searchBrdItmCdVal=&brdItmSeq=10573&searchWord=&_csrf=67b81ea4-b54a-4340-bcc4-366b330434de&pageIndex=1")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    data = soup.find('a', class_='onair')['href']

    driver.close()

    return data

if __name__ == '__main__':
    print('#{}'.format(youtube_link()))
