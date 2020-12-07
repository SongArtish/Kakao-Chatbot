'''
Description

## 1년 중 특정 날짜를 1~365 중 하나의 숫자로 반환하는 함수 ##

참고사항
- 월까지 식별하는 함수! 년은 식별X
- 2월은 28일 기준
'''

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


# 테스트 성공

# today = '2020-01-01'
# year_to_days(today)

