from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list, name='list'),
    path('read/<int:id>/', views.read, name='read'),
    path('regist/<int:id>',views.regist, name='regist'),
    path('remove/<int:id>/',views.remove, name='remove'),
]