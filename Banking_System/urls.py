from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("customer/",views.customer, name="customer"),
    path("<int:id>/money/",views.money, name="money"),
    path("<int:id>/money_processing/",views.money_processing, name="money_processing"),
    path("history/",views.history, name="history"),

]