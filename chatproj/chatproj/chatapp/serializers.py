from .models import Users,Chat
from rest_framework import serializers

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'last_visit')

class ChatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chat
        fields = ('sender', 'receiver','msg','time')