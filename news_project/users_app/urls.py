from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cat$',views.catt,name='catt'),
    url(r'^(?P<categoryn>\d+)/index', views.postcat),

]
