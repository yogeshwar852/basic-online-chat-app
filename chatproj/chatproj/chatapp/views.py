from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializer,ChatSerializer
from .models import Users,Chat
from django.shortcuts import render
import datetime
from django.utils import timezone
from django.db.models import Q


def index(request):
    return render(request, 'chat_app/index.html')

def memory(request):
    return render(request, 'chat_app/home.html')





@api_view(['POST'])
def view_users(request):
    if request.method == 'POST':     
        user, created = Users.objects.update_or_create(
            user_id=request.data['sender'],
            defaults={
                'last_visit':datetime.datetime.now(tz=timezone.utc)
            })

        time=datetime.datetime.now(tz=timezone.utc)- datetime.timedelta(seconds=15)
        data={
            'status': 'true',
            'data': UsersSerializer(Users.objects.filter(last_visit__gte=time), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)
        
    
@api_view(['POST'])
def save_msg(request):
    if request.method == 'POST':
        time=datetime.datetime.now(tz=timezone.utc)
        chat = Chat(
            sender=request.data['sender'],
            receiver=request.data['receiver'],
            msg=request.data['msg'],
            time=time
            )
        chat.save();
        data={
            'status': 'true'
        }
        return Response(data, status=status.HTTP_200_OK)   

@api_view(['POST'])
def get_chat(request):
    if request.method == 'POST':
        time=datetime.datetime.now(tz=timezone.utc)- datetime.timedelta(seconds=150)
        data={
            'status': 'true',
            'data': ChatSerializer(Chat.objects.filter(time__gte=time,receiver=request.data['sender']), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST'])
def view_msg(request):
    if request.method == 'POST':
        data={
            'status': 'true',
            'data': ChatSerializer(Chat.objects.filter(Q(receiver=request.data['sender'],sender=request.data['receiver']) | Q(receiver=request.data['receiver'],sender=request.data['sender'])), many=True).data
        }
        return Response(data, status=status.HTTP_200_OK)