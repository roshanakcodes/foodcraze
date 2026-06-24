from django.urls import path
from . import views1
urlpatterns = [
    path("", views1.fav, name="fav"),
    path('remove/<int:id>/', views1.remove_fav, name='remove_fav'),
]