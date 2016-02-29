from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'main_page',views.showposts,name='showposts'),
    url(r'^(?P<categoryn>\d+)/index', views.postcat),
    url(r'^(?P<post_id>\d+)/posts', views.getpost),
    url(r'^(\d+)/(?P<postn>\d+)/details', views.details),
    url(r'^(\d+)/(\d+)/(?P<t>\d+)/postbytag', views.postbytag),

]
