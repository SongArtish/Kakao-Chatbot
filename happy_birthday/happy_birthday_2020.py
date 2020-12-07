# import
import time, win32con, win32api, win32gui
import datetime
import schedule
import time
from library.year_to_days import year_to_days
import random
###################################
'''
Index
1. 카톡 메시지 전송 기본 코드
2. 생일 설정
3. 실행
'''
###################################
# 1. 카톡 메시지 전송 기본 코드

chatName = '김현지'


# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
    win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, text)
    SendReturn(hwndEdit)


# # 엔터
def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# # 채팅방 열기
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
# 2. 생일 설정

# 함수
def birthday(birth_month, birth_day, name, celebrate):
    open_chatroom(chatName)
    text = """{}월 {}일은 {}님의 생일입니다!
🎉생일 축하해요 {}님🎂
{}
♥서울 3반 일동♥""".format(birth_month, birth_day, name, name, celebrate)
    print(text)
    kakao_sendtext(chatName, text)

ment = [
'''
 　　　　｜
　　／￣￣￣＼
　／　　∧　　＼
　│　／ 川＼　│
　＼／┏┻┓ ＼／
 。゛＃┃생┃゛。
゛，。┃일┃＃。゛
 。゜＃┃축┃゛。゛
 ，＊。┃하┃゜。＃
＃゜。┃해┃゜＊。
　　　┃☆┃
　　　┗┯┛
 　∧∧　│
　(*´∀`)│
  　　/　⊃
''',
'''
           iiiiiiii
   ┏━♡♡━┓
 ┏"━☆━☆━"┓
 ♡-생일축하해-♡
★☆:+.♡.+:★☆
''',
'''
 ┏┓┏┓｡･ﾟﾟ･｡｡ﾟ💖
 ┃┗┛ appy💜
 ┃┏┓┃ birth✿
 ┗┛┗┛ day*ﾟ✾
 ｡.｡.｡.｡💛
''',
'''
　∧＿∧ 
（｡･ω･｡)つ━☆・*。
⊂　　 ノ 　　　・゜
　しーＪ　　　°。+ * 。
　　　　　　　　　.・゜
　　　　　　　　　゜｡ﾟﾟ･｡･ﾟﾟ。
　　　　　　　　　　ﾟ。　 　｡ﾟ
　　　　　　　　　　　ﾟ･｡･ﾟ
''',
'''
　　　　　 ♪∧,,∧
　　　♪∧,,∧・ ω・)
　∧,,∧・ ω・)　　 )っ
(・ ω・)　　 )っ＿_フ
(っ　　)っ＿_フ(_/彡
　( ＿_フ(_/彡
　 (_/彡♪
'''
]


곽민준 = {
    'birth_month': '11',
    'birth_day': '25',
    'name': '민준',
    'celebrate': random.choice(ment),
}
김현지 = {
    'birth_month': '12',
    'birth_day': '18',
    'name': '현지',
    'celebrate': random.choice(ment),
}
박예린 = {
    'birth_month': '11',
    'birth_day': '30',
    'name': '예린',
    'celebrate': random.choice(ment),
}
오민택 = {
    'birth_month': '10',
    'birth_day': '25',
    'name': '민택',
    'celebrate': random.choice(ment),
}
이대련 = {
    'birth_month': '10',
    'birth_day': '18',
    'name': '대련',
    'celebrate': random.choice(ment),
}
이도건 = {
    'birth_month': '11',
    'birth_day': '11',
    'name': '도건',
    'celebrate': random.choice(ment),
}
이형창 = {
    'birth_month': '12',
    'birth_day': '17',
    'name': '형창',
    'celebrate': random.choice(ment),
}
우진하 = {
    'birth_month': '10',
    'birth_day': '20',
    'name': '진하',
    'celebrate': random.choice(ment),
}
김경윤 = {
    'birth_month': '12',
    'birth_day': '07',
    'name': '경윤',
    'celebrate': random.choice(ment),
}
이호창 = {
    'birth_month': '12',
    'birth_day': '09',
    'name': '호창',
    'celebrate': random.choice(ment),
}


# # 2020 생일 대상자 리스트 만들기
seoul3 = [곽민준, 김현지, 박예린, 오민택, 이대련, 이도건, 이형창, 우진하, 김경윤, 이호창] 

###################################
# 3. 실행

def wake_up():
    nowTime = datetime.datetime.now().strftime('%H:%M')
    # 오늘
    today = str(datetime.date.today())

    for i in range(len(seoul3)):
        target_date = '2020-{}-{}'.format(seoul3[i].get('birth_month'), seoul3[i].get('birth_day'))
        if today == target_date:
            targer = seoul3[i]
            birthday(**targer)


if __name__ == '__main__':
    wake_up()
    # 이하 스케줄
    # schedule.every().day.at('19:00').do(wake_up)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

###################################