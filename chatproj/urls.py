from django.conf.urls import url, include
from chatapp import views
from chatapp.views import index


urlpatterns = [
    url(r'^view_users/$', views.view_users),
    url(r'^save_msg/$', views.save_msg),
    url(r'^get_chat/$', views.get_chat),
    url(r'^view_msg/$', views.view_msg),
    url(r'^index', index, name='index'),
]