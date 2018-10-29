from django.conf.urls import include, url
from django.contrib import admin
# from mysite.views import hello, current_datetime, hours_ahead, display_meta, contact, message
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^hello/', 'mysite.views.hello'), OR
    url(r'^hello/$', views.hello),
    url(r'^time$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^display$', views.display_meta),
    url(r'^', include('books.urls')),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.message),

]
