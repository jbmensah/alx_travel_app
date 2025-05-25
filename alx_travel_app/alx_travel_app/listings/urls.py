from django.urls import path
from . import views

urlpatterns = [
    # for now, you can leave this empty or add a simple test view:
    path('', views.home, name='listing-home'),
]
