"""backend URL Configuration

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
from django.urls import include, path
from properties import views as prop_views
from login import views
from recommender_system import views as rec_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/properties/', prop_views.properties_list),
    path('api/v1/properties/<int:pk>/', prop_views.property_detail),
    path('api/v1/users/register/', views.userList.createuser),
    path('api/v1/users/login/',views.loginView.loginuser),
    path("api/v1/users/logout/",views.logoutuser),
    path("log_user_activity/", rec_views.log_user_activity),
    path("user_activity_list/", rec_views.user_activity_list),
]
