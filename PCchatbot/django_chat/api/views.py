from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ChatInfo
from .serializers import ChatInfoListSerializer

# Create your views here.
@api_view(['GET'])
def get_chatinfo_list(request):
    chatInfos = ChatInfo.objects.all()
    serializer = ChatInfoListSerializer(chatInfos, many=True)
    return Response(serializer.data)
