"""studinfo URL Configuration

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
from django.urls import path
from django.conf import settings

# importing views from app
# from administrator.url import path,include
from django.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('student/', include('administrator.url')),
    # path('studentprofile', s_profile, name='studentprofile'),
    # path('s_details', s_details, name='s_details'),
    path('admin/', admin.site.urls),
]

admin.site.site_header = "Student info-sys ADMIN"
admin.site.site_title = "Student info-sys Admin Portal"
admin.site.index_title = "Welcome to Student info-sys Researcher Portal"

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
