from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register_view,name ="register-page"),
    path('login', views.login_view,name ="login-page"),
    path('logout', views.logout_view,name ="logout-page"),
    path('profile', views.profile_view,name ="profile-page"),
    path('updateProfile', views.update_profile_view,name ="updateProfile-page"),
    path('changePassword', views.password_change_view,name ="changePassword-page"),
    path('update_player_data', views.update_player_data, name='update_player_data'),
    path('registration_success/', views.registration_success, name='registration_success'),
]