from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.make_query, name='make_query'),
]

