from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User

# 首页１
def index(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'tel': user.tel})

    else:
        return render(request, 'index.html')





# 首页２
def index2(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    if users.exists():
        user = users.first()
        return render(request, 'index2.html', context={'tel': user.tel})

    else:
        return render(request, 'index2.html')


# 注册
def register(request):
    # print(1)
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # print(2)
        # 获取数据
        user = User()
        user.tel = request.POST.get('tel')
        user.password = request.POST.get('password')
        # print(user.tel, user.password)
        # 保存数据
        user.save()

        response = redirect('App:index')
        # 设置令牌
        response.set_cookie('tel', user.tel)


        return response

# 登录
def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')
    elif request.method == 'POST':
        # 获取数据
        tel = request.POST.get('tel')
        password = request.POST.get('password')
        users= User.objects.filter(tel=tel).filter(password=password)
        if users.exists():
            user= users.first()
            response=redirect('App:index')
            # 状态保持
            response.set_cookie('tel', user.tel)
            return response
        else:
            return HttpResponse('用户名或密码错误')
# 退出
def quit(request):
    response = redirect('App:index')
    #　删除令牌
    response.delete_cookie('tel')

    return response

# 商品列表
def goods(request):
    print(request.method)
    return render(request, 'goods.html')

# 购物车
def cart(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    if users.exists():
        user = users.first()
        return render(request, 'cart.html', context={'tel': user.tel})

    else:
        return render(request, 'cart.html')



def cart2(request):
    return render(request, 'cart2.html')