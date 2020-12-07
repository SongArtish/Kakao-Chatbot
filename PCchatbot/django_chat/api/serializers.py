from rest_framework import serializers
from .models import ChatInfo

class ChatInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInfo
        fields = '__all__'