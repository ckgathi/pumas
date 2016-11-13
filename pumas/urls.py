"""pumas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from pumas.views.login_view import LoginView
from pumas.views.home_view import HomeView
from pumas.views.logout_view import LogoutView


urlpatterns = [
    url(r'accounts/login', LoginView.as_view(), name='login_url'),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(), name='logout_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^upload/', include('upload.urls')),
    url(r'^download_seach_view/', include('download_view_search.urls')),
    url(r'^', HomeView.as_view(), name='home_url'),
    url(r'^home/', HomeView.as_view(), name='home_url'),
]

admin.site.site_header = 'PUMAS'
