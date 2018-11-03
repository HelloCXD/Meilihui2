from django.db import models

# Create your models here.

class Wheel(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)


class User(models.Model):
    tel = models.CharField(max_length=20)
    password = models.CharField(max_length=256)



