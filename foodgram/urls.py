"""foodgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.flatpages.views import flatpage
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("auth/", include("users.urls")),
    path('admin/', admin.site.urls),
    path("", include("api.urls")),
    path("", include("recipes.urls")),
]

urlpatterns += [
    path('about-author/', flatpage, {'url': '/about-author/'}, name='author'),
    path('about-spec/', flatpage, {'url': '/about-spec/'}, name='spec'),
]

handler404 = "recipes.views.page_not_found"
handler500 = "recipes.views.server_error"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
