from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register$', views.RegisterView.as_view()),  # 注册
    url(r'^activate/(?P<activate_key>\w+)', views.activate),  # 激活

]
