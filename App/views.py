from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User


def index(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    if users.exists():
        user = users.first()
        return render(request, 'index.html', context={'tel': user.tel})

    else:
        return render(request, 'index.html')






def index2(request):
    tel = request.COOKIES.get('tel')
    users = User.objects.filter(tel=tel)
    if users.exists():
        user = users.first()
        return render(request, 'index2.html', context={'tel': user.tel})

    else:
        return render(request, 'index2.html')



def register(request):
    # print(1)
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # print(2)
        user = User()
        user.tel = request.POST.get('tel')
        user.password = request.POST.get('password')
        # print(user.tel, user.password)
        user.save()

        response = redirect('App:index')
        response.set_cookie('tel', user.tel)


        return response


def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')
    elif request.method == 'POST':
        tel = request.POST.get('tel')
        password = request.POST.get('password')
        users= User.objects.filter(tel=tel).filter(password=password)
        if users.exists():
            user= users.first()
            response=redirect('App:index')
            response.set_cookie('tel', user.tel)
            return response
        else:
            return HttpResponse('用户名或密码错误')

def quit(request):
    response = redirect('App:index')
    response.delete_cookie('tel')

    return response


def goods(request):
    return render(request, 'goods.html')


def cart(request):
    return render(request, 'cart.html')


