"""wceac URL Configuration

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
from django.urls import path, include
from django.conf.urls import handler400, handler403, handler404, handler500
from . import views
from django.conf import settings
from django.conf.urls.static import static
handler404 = 'wceac.views.error_404'
handler500 = 'wceac.views.error_500'
handler403 = 'wceac.views.error_403'
handler400 = 'wceac.views.error_400'
urlpatterns = [
    path('aapconvincehogayeyameinaurbolu/', admin.site.urls),
    #path('admin/', admin.site.urls),
    path('', views.landing.as_view(),name='landing'),
    path('team/', include('team.urls')),
    path('blogs/', include('blogs.urls')),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
