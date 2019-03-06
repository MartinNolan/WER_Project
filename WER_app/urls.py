from django.conf.urls import url
from WER_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^review_sample/', views.review_sample, name='review_sample'),
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^contact-us/', views.contact, name='contact-us'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
]
