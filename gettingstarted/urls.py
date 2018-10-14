from django.conf.urls import include, url
from django.urls import path
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    #path('profile/addmember',TemplateView.as_view(template_name='addmember.html'),name='addmember'),
    path('profile/addmember', hello.views.getBill ,name='addmember'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('profile/',TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('register/',TemplateView.as_view(template_name='register.html'), name='register'),
    path('profile/groupinfo',TemplateView.as_view(template_name='groupinfo.html'), name='groupinfo'),
    path('profile/createbill',TemplateView.as_view(template_name='createbill.html'),name='createbill'),
    path('profile/billinfo',TemplateView.as_view(template_name='billinfo.html'),name='billinfo'),
    path('aboutus',TemplateView.as_view(template_name='aboutus.html'),name='aboutus'),
    path('admin/', admin.site.urls),
    path('about/', hello.views.about, name='about'),
]
