from django.conf.urls import url
from WER_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^review_sample/', views.review_sample, name='review_sample'),
<<<<<<< HEAD
=======
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.review, name='review'),
>>>>>>> 9966d4de5141d7bd1e73dc015bfb14da423884d8
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^contact-us/', views.contact, name='contact-us'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
    url(r'^login/', views.login, name='login'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]

