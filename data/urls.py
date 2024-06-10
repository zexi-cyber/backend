
from django.urls import  path
from . import views

urlpatterns = [
    path('add_query/', views.add_query),
    path('provide_data1/', views.provide_data1)
]
