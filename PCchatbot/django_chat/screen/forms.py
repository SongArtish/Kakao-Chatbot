from django import forms
from api.models import ChatInfo

class ChatInfoForm(forms.ModelForm):
    class Meta:
        model = ChatInfo
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={'class':'form-control col-12 mb-3', 'placeholder':'메시지를 입력하세요.', 'rows':3, "cols":5}),
            'chat_hour': forms.NumberInput(attrs={'class':'form-control col-5 mb-3', 'placeholder':'0 ~ 23'}),
            'chat_minute':forms.NumberInput(attrs={'class':'form-control col-5 mb-3', 'placeholder':'0 ~ 59'}),
            'send_to':forms.Select(attrs={'class':'form-control col-12 mb-3'})
        }

        labels = {
            'message':'보낼 메시지',
            'chat_hour':'보낼 시간(시)',
            'chat_minute': '보낼 시간(분)',
            'send_to':'보낼 곳'
        }

    