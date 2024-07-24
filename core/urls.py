from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view,name ="app-home-page"),
    path('about', views.about_view,name ="about-page"),
    path('contact', views.contact_view,name ="contact-page"),
    path('error404', views.error_404_view,name ="404-page"),
    path('error500', views.error_500_view,name ="500-page"),

]