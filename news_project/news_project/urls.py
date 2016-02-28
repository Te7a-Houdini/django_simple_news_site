"""news_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""



from django.conf.urls import url ,include




from django.contrib import admin
#New Imports

from django.conf import settings
from users_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')) #Added Uploader url
    ,url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

	
	#pplication urls
	url(r'^users_app/', include('users_app.urls')),
    # user auth urls
    url(r'^accounts/login/$', 'auth_app.views.login'),
    url(r'^accounts/auth/$', 'auth_app.views.auth_view'),
    url(r'^accounts/logout/$', 'auth_app.views.logout'),
    url(r'^accounts/loggedin/$', 'auth_app.views.loggedin'),
    url(r'^accounts/invalid/$', 'auth_app.views.invalid_login'),
    url(r'^accounts/register/$', 'auth_app.views.register_usr'),
    url(r'^accounts/register_success/$', 'auth_app.views.register_success')

]
