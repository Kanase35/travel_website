from django.urls import path
from . import views

urlpatterns = [
    path('calc/', views.calc, name = "calc") ,
    path('calc/add/', views.add, name = "add")
]
