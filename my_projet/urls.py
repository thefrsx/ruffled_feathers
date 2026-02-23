"""
URL configuration for my_projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from my_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Homepage → list of editions

    path('', views.home_page, name='home'),

    # Edition CRUD
    path('edition/', views.edition_list, name='edition_list'),
    path('edition/<int:pk>/', views.edition_detail, name='edition_detail'),
    path('edition/new/', views.edition_create, name='edition_create'),
    path('edition/<int:pk>/edit/', views.edition_edit, name='edition_edit'),
    path('edition/<int:pk>/delete/', views.edition_delete, name='edition_delete'),

    # Story CRUD
    path('story/<int:edition_pk>/new/', views.story_create, name='story_create'),
    path('story/<int:pk>/edit/', views.story_edit, name='story_edit'),
    path('story/<int:pk>/delete/', views.story_delete, name='story_delete'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='my_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Authors
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_create, name='author_create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
