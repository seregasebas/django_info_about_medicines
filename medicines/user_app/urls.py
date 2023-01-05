from django.urls import path
from user_app import views
from django.contrib.auth.views import LogoutView

app_name = 'user_app'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('updatetoken/', views.update_token, name='update_token'),
    path('update-token-ajax/', views.update_token_ajax),
]