# README.md

작성자 : 이송영

---

[TOC]

---



## 개요

> 다가오는 과목평가/월말평가 알림톡 기능을 구현한다.



## 코드 구현 과정

### 외장 라이브러리

- 본 코드를 구현하기 위해서 가져온 라이브러리는 다음과 같다.

```markdown
### requirements.txt

APScheduler==3.6.3
pytz==2020.1
pywin32==228
schedule==0.6.0
six==1.15.0
tzlocal==2.1
```

- 또한 1년 중 특정 날짜를 1~365 중 하나의 숫자로 반환하는 함수를 사용하기 위해 `year_to_days`라는 라이브러리를 작성하였다.
  - 월까지 식별하는 함수이며, 년은 식별할 수 없다.
  - 2월은 28일 기준으로 작성되었다.

```python
# library/year_to_days.py

def year_to_days(date):

    # date는 yyyy-mm-dd 형식!
    date_list = list(str(date))
    
    ## 1. 월 계산

    # 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365
    month = int(date_list[-5]) * 10 + int(date_list[-4])
    months = {
        '1' : 0,
        '2' : 31,
        '3' : 59,
        '4' : 90,
        '5' : 120,
        '6' : 151,
        '7' : 181,
        '8' : 212,
        '9' : 243,
        '10' : 273,
        '11' : 304,
        '12' : 334,
    }

    ## 2. 일 계산
    day = int(date_list[-2]) * 10 + int(date_list[-1])
    
    ## 3. 결과 값 계산
    days = months.get(str(month)) + day
    # print(days)
    return days
```

- 최종적으로 import한 라이브러리는 다음과 같다.

```python
import time, win32con, win32api, win32gui
import datetime
import schedule
import time
from library.year_to_days import year_to_days
```





### 1. 카톡 메시지 전송 기본 코드

> 카톡 메시지 전송 기본 코드는 그대로 사용한다.

- `chatName`에서 알림을 제공할 톡방을 지정한다.

```python
chatName = '이송영'
```

```python
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
```



### 2. 시험날짜 설정

- 평가 정보를 딕셔너리에 담는다.

```python
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
```

- 평가 정보를 담은 딕셔너리를 하나의 리스트로 만든다.

```python
# 평가 전체 리스트 만들기
exams = [Oct2nd, Oct3rd, OctFinal]
```

- 평가 정보를 받아서 텍스트로 단톡방에 출력할 `exam` 함수를 만든다.

```python
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
```



### 3. 실행

- 위에 작성한 시험 정보를 가져와 남은 날짜를 계산한다.
- 그리고 가장 가까운 단 1개의 평가에 대해서만 알림을 해주는 코드를 구현하였다.
- 제일 밑의 `if __name__ == '__main__':` 이하의 주석 처리된 코드를 처리하면 매일 특정 시간에 알림 메시지를 보내도록 조작할 수 있다.

```python
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
```



## 구현 일지



### 2020년 10월 5일

#### 구현한 기능

- 다가오는 평가에 대한 알림 기능
- D-day count 기능



#### 보완할 점

- D-day를 계산할 때, 마지막 2자리의 일자만 계산하기 때문에, 다음달을 넘어가게 되면 계산이 안 된다.
  - 보완 방법
    1. 월별로 하드코딩을 하면 가능
    2. 간단하게 다음달까지는 (한 번) 계산할 수 있는 알고리즘을 만든다.
    3. 1년을 1~365 숫자로 변환해주는 라이브러리를 찾거나 만든다. (**유력**:star:)
- 알고리즘을 더욱 간소화하면 좋을 것 같다. (다소 지저분하다.)



### 2020년 10월 6일

#### 보완한 점
- 1년을 1~365 숫자로 변환해주는 라이브러리 `year_to_day`를 만들어서 동일 년도에서는 D-day를 정확하게 계산할 수 있는 방식을 구축하였다.



## 한계

- 알고리즘을 더욱 간소화 및 효율화 할 수 있는 방안을 간구하면 좋을 것이다.
- 시험 정보를 담은 라이브러리를 직접 입력해주어야 한다.
  - 더욱 자동화를 위해서는 크롤링을 할 수 있을 것이다.