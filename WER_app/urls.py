from django.conf.urls import url
from WER_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^review_sample/', views.review_sample, name='review_sample'),
    url(r'^base/', views.base, name='base'),
    
]