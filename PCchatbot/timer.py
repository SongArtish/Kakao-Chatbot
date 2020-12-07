import time, win32con, win32api, win32gui
# 시간 맞춰 메시지 보내기용
import datetime
import schedule
import time
################################
# # 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = 'SSAFY 4기 서울 3반(A반)'
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

def main():
    open_chatroom(kakao_opentalk_name)  # 채팅방 열기

#     text = """~ 8:59 까지 
# 👉 입실체크
# 👉 건강설문
# - 온라인/오프라인 제대로 체크하기
# - 체온체크 (온라인시 “온라인 수업일” 로 체크하기)
# https://edu.ssafy.com/
# """
    text = """👉 퇴실체크
👉 건강설문"""
    kakao_sendtext(kakao_opentalk_name, text)    # 메시지 전송


def wake_up():
    nowTime = datetime.datetime.now().strftime('%H:%M')
    main()

if __name__ == '__main__':
    schedule.every().day.at('18:00').do(wake_up)
    while True:
        schedule.run_pending()
        time.sleep(1)