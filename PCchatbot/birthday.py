import json
from datetime import datetime
from random import choice
from kakao_api import kakao_sendtext, open_chatroom


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


# 1가지 정보만 가져와서 1번만 실행하면 됨
def happy_birthday():

    this_month = datetime.now().month
    this_day = datetime.now().day

    birthday_result = []

    with open('birthday.json', 'r', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        # 파일 내 birthday 배열 읽기
        for birthday in json_data['birthday']:
            if int(birthday['birth_month']) == this_month and int(birthday['birth_day']) == this_day:
                birthday_result.append(birthday)

    birthday_message = []

    for birthday in birthday_result:
        # 메시지 생성
        message = """{}월 {}일은 {}님의 생일입니다!
    🎉생일 축하해요 {}님🎂
    {}
    ♥서울 3반 일동♥""".format(birthday['birth_month'], birthday['birth_day'], birthday['name'], birthday['name'], choice(ment))
        birthday_message.append(message)

    return birthday_message

        # # 보내는 곳
        # open_chatroom("#잡담방 SSAFY 4기 3(A)반")
        # # 보내기!
        # kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", message)


if __name__ == '__main__':
    print(happy_birthday())