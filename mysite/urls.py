"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from mysite.views import current_datetime, hours_ahead, display_meta, contact
from . import views
from books import views
from books.views import PublisherList, PublisherDetail
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', my_homepage_view),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^info/$', display_meta),
    url(r'^contact/$', contact),
    #url(r'^search_form/$', views.search_form),
    url(r'^search/$', views.search), # books/view.py
    url(r'^publishers/$', PublisherList.as_view()),
    url(r'^publisher/(?P<slug>[-\ \'\w]+)/$', PublisherDetail.as_view()), #en lugar de slug_filed puedo usar pk (clave)

]

#if settings.DEBUG:
   # urlpatterns += [url(r'^debuginfo/$', views.debug),] #no existe esta vista
