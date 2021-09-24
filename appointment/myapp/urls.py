from django.urls import path
from.import views

urlpatterns = [
    path('chat/',views.home,name='home')
]