from . import views
from django.urls import path

urlpatterns = [
    # path('register', views.register_view,name ="register-page"),
    path('progress',views.view_progress, name = "progress-page")
]