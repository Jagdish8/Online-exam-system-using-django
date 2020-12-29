from django.contrib import admin
from django.urls import path,include
from onlineapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('mains',views.mains,name="mains"),
    path('maint',views.maint,name="maint"),
    path('logout',views.logoutuser,name="logout"),
    path('addpaper',views.addpapers,name="addpaper"),
    path('taketest',views.taketest,name="taketest"),
    path('question2',views.question2,name='question2'),
    path('question3',views.question3,name='question3'),
    path('question4',views.question4,name='question4'),
    path('question5',views.question5,name='question5'),
    path('question6',views.question6,name='question6'),
    path('question7',views.question7,name='question7'),
    path('question8',views.question8,name='question8'),
    path('question9',views.question9,name='question9'),
    path('question10',views.question10,name='question10'),
    path('finalscore',views.finalscore,name='finalscore'),
    
]