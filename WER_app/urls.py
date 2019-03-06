from django.conf.urls import url
from WER_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^review_sample/', views.review_sample, name='review_sample'),
<<<<<<< HEAD
    url(r'^base/', views.base, name='base'),
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^contact-us/', views.contact, name='contact-us'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
]
>>>>>>> 04f957e3dbafa8ceba2e6608bfbc2706021bbeaf
