from django.conf.urls import url, include
from .views import Register, activate, upload_avatar

urlpatterns = [
    url(r'^register$', Register.as_view(), name='register'),  # 注册
    url(r'^activate/(?P<activate_key>\w+)$', activate, name='activate'),  # 激活
    url(r'^upload_avatar$', upload_avatar, name='upload_avatar')
]