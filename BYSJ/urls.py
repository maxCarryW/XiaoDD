"""BYSJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include

import xadmin

from base.views import Pagination

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/', include('users.urls', namespace='admin')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^pagination/', Pagination.as_view(), name='pagination'),
    url(r'', include('visit.urls', namespace='visit')),
]

handler404 = 'manage.views.page_not_found'