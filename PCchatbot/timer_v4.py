import schedule
import time
from kakao_api import open_chatroom, kakao_sendtext
from birthday import happy_birthday
from exam import study_exam
from crawl import youtube_link


def send_birthday():
    birthday_list = happy_birthday()
    for birthday in birthday_list:
        # 보내는 곳
        open_chatroom("#잡담방 SSAFY 4기 3(A)반")
        # 보내기!
        kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", birthday)


def send_exam():
    exam_message = study_exam()
    # 보내는 곳
    open_chatroom("#잡담방 SSAFY 4기 3(A)반")
    # 보내기!
    kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", exam_message)


def send_exit():
    text = """👉 퇴실체크
    👉 건강설문"""
    # 보내는 곳
    open_chatroom("#잡담방 SSAFY 4기 3(A)반")
    # 보내기!
    kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", text)


def send_enter():
    text = """~ 8:59 까지 
    👉 입실체크
    👉 건강설문
    - 온라인/오프라인 제대로 체크하기
    - 체온체크 (온라인시 “온라인 수업일” 로 체크하기)
    https://edu.ssafy.com/
    """
    # 보내는 곳
    open_chatroom("#잡담방 SSAFY 4기 3(A)반")
    # 보내기!
    kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", text)

def send_link():
    link = youtube_link()
    text = "강의 링크는 {} 야. \n오늘도 수업 열심히 듣자:)".format(link)
    # 보내는 곳
    open_chatroom("#잡담방 SSAFY 4기 3(A)반")
    # 보내기!
    kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", text)

if __name__ == '__main__':
    # 생일 축하 보내기
    # 혹시 모를 딜레이 방지를 위해 00시 01분
    schedule.every().day.at('00:01').do(send_birthday)
    # 시험공부는 저녁은 먹고 해야지
    schedule.every().day.at('19:30').do(send_exam)
    # 입실, 퇴실체크
    schedule.every().day.at('08:30').do(send_enter)
    schedule.every().day.at('18:00').do(send_exit)
    # 링크 보내기
    schedule.every().day.at('09:27').do(send_link)
    schedule.every().day.at('13:57').do(send_link)

    while True:
        schedule.run_pending()
        time.sleep(1)