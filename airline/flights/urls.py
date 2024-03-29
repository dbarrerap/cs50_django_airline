from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:flight_id>', views.flight, name='details'),
    path('book/<int:flight_id>', views.book, name='book'),
]