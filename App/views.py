from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User, Wheel, Goodslist


# 首页１
def index(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    wheels = Wheel.objects.all()
    # print(wheels)

    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'tel': user.tel, 'wheels': wheels})

    else:
        return render(request, 'index.html', context={'wheels': wheels})





# 首页２
def index2(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    goods = Goodslist.objects.all()
    print(goods)
    if users.exists():
        user = users.first()
        print(1)
        return render(request, 'index2.html', context={'tel': user.tel, 'goods':goods})

    else:
        print(2)
        return render(request, 'index2.html', context={'goods':goods})


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

        try:
            user= User.objects.filter(tel=tel).first()

            if user.password != password:
                return render(request, 'login.html', context={'error': '密码错误'})
            else:
                response=redirect('App:index')
                response.set_cookie('tel', user.tel)
                return response

        except:
            return render(request, 'login.html', context={'error': '电话错误，请重新输入'})

# 退出
def quit(request):
    response = redirect('App:index')
    #　删除令牌
    response.delete_cookie('tel')

    return response

# 商品列表
def goods(request):
    print(1)
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


def checkin(request):
    tel= request.GET.get('tel')
    print(tel)
    responseData = {
        'msg': '电话可用',
        'status': 1
    }

    tels = User.objects.filter(tel=tel)
    if tels:
        print(tels)
        responseData['msg'] = '电话已被注册'
        responseData['status'] = -1
        return JsonResponse(responseData)
    else:
        # print('else'+tels)
        return JsonResponse(responseData)


# def checkon(request):
#     tel=request.GET.get('tel')
#     print(tel)
#     tels = User.objects.filter(tel=tel)
#     return JsonResponse({'msg': '电话可用'})