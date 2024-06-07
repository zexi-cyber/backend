
from django.urls import  path
from . import views

urlpatterns = [
    path('add_query/', views.add_query)
]
