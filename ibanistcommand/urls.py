from django.contrib import admin
from django.urls import path, include
from .views import ibanisthesabtosheba,ibanistshebatohesab, ibanisthesabtosheba_keshavarzi,ibanisthesabtosheba_refah,ibanisthesabtosheba_tejarat

urlpatterns = [
    path('hesab/', ibanisthesabtosheba, name='hesabtosheba'),
    path('shaba/', ibanistshebatohesab, name='shebatohesab'),
    path('banks/keshavarzi/', ibanisthesabtosheba_keshavarzi, name='keshavarzi'),
    path('banks/tejarat', ibanisthesabtosheba_tejarat, name='tejarat'),
    path('banks/refah', ibanisthesabtosheba_refah, name='refah'),

]
