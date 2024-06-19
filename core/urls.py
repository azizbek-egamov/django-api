"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from main.views import *
from django.views.defaults import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name="home"),
    path('logout/', LogoutPage, name='logout'),
    path('login/', LoginPage, name='login'),
    path('signup/', SignupPage, name='signup'),
    path('categorys/', CategorysPage, name='category'),
    path('category/<slug:slug>/', BooksPage, name='categorys'),
    path('book/<slug:category>/<int:slug>/', Book, name='book'),
    path('kitoblar/', kitoblar_list, name='kitoblar_list'),
    path('search/', SearchPage, name='search'),
    path('api/', include('api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
