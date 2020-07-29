"""monospharma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls import include, url
from src.base.models import poll, humanresource
from src.accounts import views as user_views
from src.courses import views as courses_views
from src.news import views as news_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', poll.home, name='poll'),
    path('vote/<poll_id>/', poll.vote, name='vote'),
    path('results/<poll_id>/', poll.results, name='results'),
    path('humanr/', humanresource.application, name='application'),
    path('', include('src.accounts.urls')),
    path('', include('src.courses.urls')),
    path('', include('src.news.urls')),
    path('', include('src.product.urls')),

]