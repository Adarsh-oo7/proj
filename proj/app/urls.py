from django.urls import path 
from . import views

urlpatterns=[
    path('',views.main,name="main"),
    path('sum',views.index,name="sum"),
    path('factoril',views.factoril,name="factoril"),
    path('percentage',views.percentage,name="percentage")
]