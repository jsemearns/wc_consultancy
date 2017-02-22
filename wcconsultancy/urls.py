"""wcconsultancy URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from main import views as main_views

urlpatterns = [
    url(r'^university/$',
        main_views.UniversityTemplateView.as_view(),
        name='universities'
    ),
    url(r'^university/(?P<id>\d+)/$',
        main_views.UniversityDetailTemplateView.as_view(),
        name='university-detail'
    ),
    url(r'^pizzapasta/',
        admin.site.urls
    ),
    url(r'^$',
        main_views.HomeTemplateView.as_view(),
        name='index'
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
