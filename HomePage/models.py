# from asyncio.windows_events import NULL
from tokenize import Name
from django.db import models

# Create your models here.
class Friends(models.Model):
    Friend_Name=models.CharField(max_length=100)

class NewUser(models.Model):
    Name=models.CharField(max_length=100,default='abc')
    Password=models.CharField(max_length=100,default='abc')
    Phone=models.BigIntegerField(default=100)
    Email=models.EmailField(max_length=50,default="abc@xyz.com")
    No_of_Friends=models.IntegerField(default=0)
    Friend_Requests=models.IntegerField(default=0)
    DB_ID_of_the_requester=models.IntegerField(default=0)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class Friend_Requests(models.Model):
    DB_ID_of_the_requester=models.ForeignKey(NewUser,on_delete=models.CASCADE,default=0)
    Request_Sent_To=models.CharField(max_length=100)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)