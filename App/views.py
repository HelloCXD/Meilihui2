from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def index2(request):
    return render(request, 'index2.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def goods(request):
    return render(request, 'goods.html')


def cart(request):
    return render(request, 'cart.html')