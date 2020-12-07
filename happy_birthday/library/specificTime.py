import datetime
import schedule # schedule pip는 설치해야 한다.
import time

def work():
    # 현재 시간
    # strftime()으로 시간 형식 지정
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')
    print(nowTime)

# 빌드테스트
# if __name__ == '__main__':
#     work()

schedule.every().day.at("19:19:00").do(work)

while True:
    schedule.run_pending()
    time.sleep(0.1)

