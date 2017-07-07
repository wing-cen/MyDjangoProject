"""MyDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from student.views import showInfo, showLoginPage, UserLogin ,checkInput, create_code_img, loginout

from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', showLoginPage),
    url(r'^showInfo/', showInfo),
    url(r'^checkInput$', checkInput),
    url(r'^loginout$', loginout),
    url(r'^create_code_img',create_code_img),
    url(r'^UserLogin$', UserLogin), #还要匹配后面的AJAX数据所以不能这样写r'^UserLogin/' 报500错误
]

