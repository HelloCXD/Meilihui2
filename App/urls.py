from django.conf.urls import url

from App import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^goods/$', views.goods, name='goods'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^quit/$',views.quit, name='quit')

]