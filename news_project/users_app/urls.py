from django.conf.urls import url
from . import views


#urlpatterns = [url(r'^$', views.index, name='index'),
#url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#url('^list$', views.list, name='list'),
#url(r'^new$', views.Question_new,name='Questions'),
#url(r'^c$', views.choice_new, name='choices'),
#url(r'^clist$', views.choice_list, name='choice_list'),

#url(r'^edit/(?P<question_id>[0-9]+)/$', views.edit_Question,name='Question_edit'),
#url(r'^editc/(?P<question_id>[0-9]+)/$', views.edit_choice,name='choice_edit'),
#url(r'^delete/(?P<question_id>[0-9]+)/$', views.delete),

#]

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

