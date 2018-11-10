from django.db import models

# Create your models here.

class Wheel(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)

class Goodslist(models.Model):
    # "id": "product1",
    # "buyer": "买手推荐",
    # "src1": "'/static/img/product1_1.jpg'",
    # "src2": "'/static/img/product1_2.jpg'",
    # "src3": "'/static/img/product1_3.jpg'",
    # "title": "红色荔枝纹拉链手提肩包",
    # "name": "Tory Burch",
    # "price": "￥2,440 ",
    # "original_price": "￥4,880",
    # "index1": "'/static/img/product1_1_s.jpg'",
    # "index2": "'/static/img/product1_2_s.jpg'",
    # "index3": "'/static/img/product1_3_s.jpg'"
    goodsid=models.CharField(max_length=20)
    buyer=models.CharField(max_length=20)
    src1=models.CharField(max_length=100)
    src2=models.CharField(max_length=100)
    src3=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=40)
    original_price=models.CharField(max_length=40)
    index1=models.CharField(max_length=100)
    index2=models.CharField(max_length=100)
    index3=models.CharField(max_length=100)


class Goodsdetail(models.Model):
    goodsid = models.CharField(max_length=20)
    buyer = models.CharField(max_length=20)
    src1 = models.CharField(max_length=100)
    src2 = models.CharField(max_length=100)
    src3 = models.CharField(max_length=100)
    src4 = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    original_price = models.DecimalField(max_digits=7, decimal_places=2)
    index1 = models.CharField(max_length=100)
    index2 = models.CharField(max_length=100)
    index3 = models.CharField(max_length=100)
    index4 = models.CharField(max_length=100)


class User(models.Model):
    tel = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=256)


class Cart(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 商品
    goods = models.ForeignKey(Goodsdetail)
    # 商品数量(选择)
    number = models.IntegerField()
    # 是否选中
    isselect = models.BooleanField(default=True)



