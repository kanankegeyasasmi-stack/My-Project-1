from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('booking/', views.booking_page, name='booking'),
    path('our_team/', views.our_team, name='our_team'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]
