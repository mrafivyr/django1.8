from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^search-form/$', views.search_form),
                url(r'^search/$', views.search)
]
