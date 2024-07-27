from . import views
from django.urls import path

urlpatterns = [
    # path('register', views.register_view,name ="register-page"),
    path('comparision_view',views.comparison_view,name='comparision-page')

]