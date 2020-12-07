from django.db import models

# Create your models here.
class ChatInfo(models.Model):
    # 보낼 메시지
    message = models.TextField()
    # 보낼 시간 (시, 24시간 기준)
    chat_hour = models.IntegerField()
    # 보낼 시간 (분)
    chat_minute = models.IntegerField()
    # 보낼 카톡방 이름 리스트
    kakao_options = [
        ('SSAFY 4기 서울 3반(A반)', 'SSAFY 4기 서울 3반(A반)'),
        ('#잡담방 SSAFY 4기 3(A)반', '#잡담방 SSAFY 4기 3(A)반'),
        ('구본혁', '구본혁'),
        ('챗봇 스터디', '챗봇 스터디'),
    ]
    # 보낼 곳
    # 기본값 = 구본혁(테스트용)
    send_to = models.CharField(max_length=50, choices=kakao_options, default='구본혁')