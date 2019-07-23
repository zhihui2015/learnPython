"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

"""
    解决导入同一工程不同文件夹内的文件的问题，
    1 添加完这两句代码:
    import sys
    sys.path.append("..")
    2 在该文件的文件夹右键点击选择"Mark Directory as"点击Exclusion
"""
import sys
sys.path.append("..")
from helloapp import views

urlpatterns = [
    path('index2/', include('hello2app.urls')),
    path('index/', views.hello),
    path('admin/', admin.site.urls)
]
