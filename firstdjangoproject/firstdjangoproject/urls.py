"""
URL configuration for firstdjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from firstdjangoproject import views

# urlpatterns = [
#     path('admin-panel/', admin.site.urls),
#     path("", views.aboutUS),
#     path('blog/<int:courseid>/', views.blog),  # dynamic routing with int
#     path('article/<slug:slug>/', views.article),  # dynamic routing with slug
#     path('user/<str:username>/', views.user_profile),  # dynamic routing with str
#]

from django.contrib import admin
from django.urls import path
from firstdjangoproject import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('contactus/', views.contactus),
]
