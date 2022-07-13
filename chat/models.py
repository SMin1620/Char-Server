from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField('채팅방 이름', max_length=100)

    class Meta:
        db_table = 'room'


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField('메세지 내용')
    created_at = models.DateTimeField('생성 날짜', auto_now_add=True)

    class Meta:
        db_table = 'message'

