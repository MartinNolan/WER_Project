from django.conf.urls import url
from WER_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^restaurant/', views.restaurant, name='restaurant'),
    url(r'^onCampus/', views.onCampus, name='onCampus'),
    url(r'^offCampus/', views.offCampus, name='offCampus'),
  #  url(r'^restaurant/', views.review_sample, name='review_sample'),
    url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.review, name='review'),
    url(r'^add_review/(?P<page_name_slug>[\w\-]+)/$', views.add_review, name='add_review'), 
    url(r'^about/', views.about, name='about'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^contact-us/', views.contact, name='contact-us'),
    url(r'^t&cs/', views.tAndC, name='t&cs'),
   #url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),

]

