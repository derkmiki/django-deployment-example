from django.conf.urls import url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]
