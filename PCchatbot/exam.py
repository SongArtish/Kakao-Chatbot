import json
from datetime import datetime

week_date = ['월', '화', '수', '목', '금', '토', '일', ]

def study_exam():
    today = datetime.now()
    exam_list = []
    with open('exam.json', 'r', encoding='UTF8') as json_file:
        json_data = json.load(json_file)
        for exam in json_data['exam']:
            exam_date = datetime.strptime(exam['exam_date'], '%Y-%m-%d')
            if exam_date > today:
                exam['left_date'] = (exam_date - today).days + 1
                exam['weekday'] = week_date[exam_date.weekday()]
                exam_list.append(exam)

    min_date = 50
    closest_exam = {}

    for exam in exam_list:
        if min_date > exam['left_date']:
            min_date = exam['left_date']
            closest_exam = exam

    if closest_exam != {}:
        exam_month = closest_exam['exam_date'][5:7]
        exam_day = closest_exam['exam_date'][8:]
        exam_message = """{} {}일 남았다!!
        {} 공부하자~~!!

        👉 {}/{}({}) 과목평가
        평가일시 : {}
        평가과목 : {}""".format(closest_exam['exam_type'], closest_exam['left_date'], closest_exam['exam_subject'],
                                exam_month, exam_day, closest_exam['weekday'], closest_exam['exam_time'], closest_exam['exam_subject'])

    return exam_message

        # # 보내는 곳
        # open_chatroom("#잡담방 SSAFY 4기 3(A)반")
        # # 보내기!
        # kakao_sendtext("#잡담방 SSAFY 4기 3(A)반", message)

if __name__ == '__main__':
    print(study_exam())