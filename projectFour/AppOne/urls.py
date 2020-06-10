from django.conf.urls import url
from django.urls import path, include
from AppOne import views

# for template tagging, django will look for app_name

app_name = 'AppOne'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    path('base/', views.base, name='base'),
    path('other/', views.other, name='other'),

]
