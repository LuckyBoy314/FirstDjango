"""forum2 URL Configuration

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
from .views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^article/', include('article.urls')),#, namespace='article')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^comment/', include('comment.urls')),
    url(r'^message/', include('message.urls')),

    # 登录 login
    # 登出 logout
    # 修改密码
    # 重置密码
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^admin/', admin.site.urls),

]

# 禁掉后台管理中的真实删除按钮
admin.site.disable_action('delete_selected')