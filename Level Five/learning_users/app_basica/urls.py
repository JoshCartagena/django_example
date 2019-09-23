from django.urls import path
from app_basica import views

# templates urls
app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]
