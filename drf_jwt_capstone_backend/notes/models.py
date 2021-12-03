from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth import get_user_model
User=get_user_model()






# Create your models here.

class Note_Type(models.Model):
    type_name = models.CharField(max_length=50)


class Notes(models.Model):
    note_name = models.CharField(max_length=50)
    note= models.CharField(max_length=500)
    note_type=models.ForeignKey(Note_Type ,on_delete=models.CASCADE)
    user= models.ForeignKey(User,on_delete=models.CASCADE)


