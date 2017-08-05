from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^help$', views.help, name = 'help'),
    url(r'^users$', views.users, name= 'user')

]
