from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views
from .views import *


urlpatterns = [
    path('', views.home, name="home"),
    path('category/<int:cid>/', show_category_page),
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)