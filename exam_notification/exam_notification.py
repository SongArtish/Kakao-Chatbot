import time, win32con, win32api, win32gui
import datetime
import schedule
import time
from library.year_to_days import year_to_days


# 1. 카톡 메시지 전송 기본 코드

chatName = '이송영'


# 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)


# 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 채팅방 열기
def open_chatroom(chatroom_name):
    # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    hwndkakao = win32gui.FindWindow(None, "카카오톡")
    hwndkakao_edit1 = win32gui.FindWindowEx( hwndkakao, None, "EVA_ChildWindow", None)
    hwndkakao_edit2_1 = win32gui.FindWindowEx( hwndkakao_edit1, None, "EVA_Window", None)
    hwndkakao_edit2_2 = win32gui.FindWindowEx( hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
    hwndkakao_edit3 = win32gui.FindWindowEx( hwndkakao_edit2_2, None, "Edit", None)

    # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
    win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
    time.sleep(1)   # 안정성 위해 필요
    SendReturn(hwndkakao_edit3)
    time.sleep(1)

###################################
# 2. 시험날짜 설정

# 함수
def exam(exam_type, exam_date, exam_time, exam_subject, count_days):
    open_chatroom(chatName)
    text = """{} {}일 남았다!!
{}공부하자~~!!

👉 10/12(월) 과목평가
평가일시 : {}
평가과목 : {}""".format(exam_type, count_days, exam_subject, exam_date, exam_subject)
    print(text)
    kakao_sendtext(chatName, text)

# 10월 2주차 과목평가
Oct2nd = {
    'exam_type' : '과목평가',
    'exam_date' : '2020-10-12',
    'exam_time' : '9시 ~ 10시 (1h)',
    'exam_subject' : '데이터베이스',
}

# 10월 3주차 과목평가
Oct3rd = {
    'exam_type' : '과목평가',
    'exam_date' : '2020-10-21',
    'exam_time' : '9시 ~ 10시 (1h)',
    'exam_subject' : '자바스크립트',
}

# 10월 월말평가
OctFinal = {
    'exam_type' : '월말평가',
    'exam_date' : '2020-10-26',
    'exam_time' : '14시 ~ 17시 (3h)',
    'exam_subject' : '알고리즘',
}


# 평가 전체 리스트 만들기
exams = [Oct2nd, Oct3rd, OctFinal]




###################################
# 3. 실행

def wake_up():
    nowTime = datetime.datetime.now().strftime('%H:%M')
    # 오늘
    today = str(datetime.date.today())

    # 시험일
    for i in range(len(exams)):
        target = exams[i]
        target_date = exams[i].get('exam_date')
        # 남은 날짜 계산
        count_days = year_to_days(target_date) - year_to_days(today)
        if count_days < 0:
            pass
        else:
            target['count_days'] = count_days
            # 실행
            exam(**target)
            # 여기 break를 걸어서 제일 가까운 시험 하나만
            # 알림되도록!!!
            break

if __name__ == '__main__':
    wake_up()
    # 이하 스케줄
    # schedule.every().day.at('19:00').do(wake_up)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

###################################