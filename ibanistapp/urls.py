from django.contrib import admin
from django.urls import path, include
from .views import IbanistView, BanksView

urlpatterns = [
    path('', IbanistView.as_view(), name='home'),
    path('banks/', BanksView.as_view(), name='banks'),

]
