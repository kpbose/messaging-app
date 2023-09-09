from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('signin', views.signin,name='signin'),
    path('signout', views.signout,name='signout'),
    path('profile', views.profile,name='profile'),
    path('requests',views.requests,name="requests"),
    path('makefreinds',views.makefreinds,name="makefreinds"),
    path('send_request/<receiver>',views.send_request,name="send_request"),
    path('accept/<sender>',views.accept,name="accept"),
    path('send/<receiver>',views.send,name="send"),
    # path('messenger', views.messenger,name='messenger'),
    path('messenger/<username>',views.messenger)
]
