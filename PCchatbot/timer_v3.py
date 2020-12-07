import time, win32con, win32api, win32gui
# 시간 맞춰 메시지 보내기용
import datetime
import schedule
import time
import requests
import json
from random import choice
################################
# API를 가져올 URL
# api_url = 'https://chatbotkakao.herokuapp.com/api/'

# # 카톡창 이름, (활성화 상태의 열려있는 창)
#  kakao_opentalk_name = 'SSAFY 4기 서울 3반(A반)'
#kakao_opentalk_name = '구본혁'


# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, text):
    # # 핸들 _ 채팅방
    hwndMain = win32gui.FindWindow( None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx( hwndMain, None, "RichEdit50W", None)
    # hwndListControl = win32gui.FindWindowEx( hwndMain, None, "EVA_VH_ListControl_Dblclk", None)

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

# 결과를 담을 배열
result = []
birthday_result = []
exam_result = []


# 서버에서 저장된 API 받아오기
def get_api():
    # API 주소
    address = 'https://chatbotkakao.herokuapp.com/api/'
    # 리스트 형태로 온다.
    chatInfos = requests.get(address).json()
    # 리스트 비우기
    result[:] = []
    
    # 리스트에 딕셔너리 객체 넣어주기
    for chatInfo in chatInfos:
        chat_hour = str(chatInfo['chat_hour'])
        chat_minute = str(chatInfo['chat_minute'])
        if 0 <= chatInfo['chat_hour'] <= 9:
            chat_hour = '0'+str(chatInfo['chat_hour'])
        if 0 <= chatInfo['chat_minute'] <= 9:
            chat_minute = '0'+str(chatInfo['chat_minute'])

        new_dict = {
            'message':chatInfo['message'],
            'chat_time':chat_hour+':'+chat_minute,
            'send_to': chatInfo['send_to']
        }

        result.append(new_dict)

# 생일 축하 멘트
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

week_date = ['월', '화', '수', '목', '금', '토', '일', ]


# 서버에 저장된 메시지 보내기
def send_message():
    global result, birthday_result, exam_result
    # 현재 시각
    nowTime = datetime.datetime.now().strftime('%H:%M')
    #오늘 날짜
    nowDate = datetime.datetime.now().strftime('%m-%d')
    # 리스트가 비어있거나 현재 시각이 새벽 5시 30분일때 서버 통신
    # 매일 보내는 메시지
    if len(result) == 0 or nowTime == '05:30':
        get_api()
        print("API 다운로드!!")
    print(result)
    # 리스트가 비어있지 않을 때 작동
    if len(result) > 0:        
        # 서버에 있는 각 정보 뜯기
        for chatInfo in result:
            # 시간이 일치한다면
            if chatInfo['chat_time'] == nowTime:
                # 저장된 카톡방 열기
                open_chatroom(chatInfo['send_to'])
                # 메시지 입력후 전송
                kakao_sendtext(chatInfo['send_to'], chatInfo['message'])

    ################################################################################################################

    # 생일 메시지, 자정을 기준으로 구동
    if len(birthday_result) == 0 or nowTime == '00:00':
        # 리스트 비우기
        birthday_result[:] = []
        # Json 파일 읽어오기
        with open('birthday.json', 'r', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            birthday_result = json_data['birthday']
            for birthday in birthday_result:
                birthday['count'] = 0
    # 반복 돌기
    for birthday in birthday_result:
        # Json에서 날짜 만들기
        birthdate = birthday['birth_month'] + '-' + birthday['birth_day']
        # 오늘 날짜이면서 아직 메시지 보낸적 없음
        if birthdate == nowDate and birthday['count'] == 0:
            # 메시지 보냈다고 표시
            birthday['count'] += 1
            # 메시지 생성
            message = """{}월 {}일은 {}님의 생일입니다!
🎉생일 축하해요 {}님🎂
{}
♥서울 3반 일동♥""".format(birthday['birth_month'], birthday['birth_day'], birthday['name'], birthday['name'], choice(ment))
            # 보내는 곳
            open_chatroom("#잡담방 SSAFY 4기 3(A)반")
            # 보내기!
            kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", message)

################################################################################################################

    # 시험 일정!
    if len(exam_result) == 0 or nowTime == '18:00':
        # 리스트 비우기
        exam_result[:] = []
        # Json 파일 읽어오기
        with open('exam.json', 'r', encoding='UTF8') as json_file:
            json_data = json.load(json_file)
            exam_result = json_data['exam']
            for exam in exam_result:
                exam['count'] = 0
    
        # 가장 가까이에 있는 시험만 출력해야한다.
        closest_exam_date = ""
        closest_exam = {}

        # 배열 반복
        for exam in exam_result:
            # 날짜가 공란이거나 더 가까운 시험이 있으면
            if closest_exam_date == "" or (time.mktime(datetime.datetime.strptime(exam['exam_date'], "%Y-%m-%d").timetuple()) < time.mktime(datetime.datetime.strptime(closest_exam_date, "%Y-%m-%d").timetuple()) and datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d') >= datetime.datetime.strptime(closest_exam_date, '%Y-%m-%d')):
                # 대체
                closest_exam_date = exam['exam_date']
                closest_exam = exam
                continue
            
        # 남은 날짜 계산
        count_days = -1
        if closest_exam_date != "":
            count_days = datetime.datetime.strptime(closest_exam_date, '%Y-%m-%d') - datetime.datetime.strptime(datetime.datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')    
        
            exam_message = """{} {}일 남았다!!
        {} 공부하자~~!!

        👉 {}/{}({}) 과목평가
        평가일시 : {}
        평가과목 : {}""".format(closest_exam['exam_type'], count_days.days, closest_exam['exam_subject'], closest_exam_date[5:7], closest_exam_date[8:], week_date[datetime.datetime.strptime(closest_exam_date, '%Y-%m-%d').weekday()], closest_exam_date, closest_exam['exam_subject'])

            if closest_exam['count'] == 0:
                print(closest_exam['count'])
                closest_exam['count'] += 1
                # 보내는 곳
                open_chatroom("#잡담방 SSAFY 4기 3(A)반")
                # 보내기!
                kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", exam_message)

################################################################

    # 1분 뒤에 다시 뵙겠습니다.
    time.sleep(60)
    # 다시 돌기
    send_message()


# def main():
#     open_chatroom(kakao_opentalk_name)  # 채팅방 열기

#     text = """~ 8:59 까지 
# 👉 입실체크
# 👉 건강설문
# - 온라인/오프라인 제대로 체크하기
# - 체온체크 (온라인시 “온라인 수업일” 로 체크하기)"""
# #     text = """👉 퇴실체크
# # 👉 건강설문"""
#     kakao_sendtext(kakao_opentalk_name, text)    # 메시지 전송


# def wake_up():
#     nowTime = datetime.datetime.now().strftime('%H:%M')
#     main()

if __name__ == '__main__':
    # send_message(get_api(api_url))
    send_message()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
        
    

    # schedule.every().day.at('08:30').do(wake_up)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)