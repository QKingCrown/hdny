from django.contrib import admin
from django.urls import path
from App import views
from django.conf.urls import url,include


urlpatterns = [
  url(r'one_data',views.one_data),
  url(r'search_form',views.search_form),
  url(r'search',views.search)
]