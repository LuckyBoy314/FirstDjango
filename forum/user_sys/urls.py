from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.RegisterView.as_view()),
    url(r'^activate/(?P<activate_key>\w+)', views.activate),
]
