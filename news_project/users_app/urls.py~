from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^cat$',views.showposts,name='showposts'),
    url(r'^(?P<categoryn>\d+)/index', views.postcat),
    url(r'^(?P<post_id>\d+)/posts', views.getpost),

]
