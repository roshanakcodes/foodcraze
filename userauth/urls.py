from . import views
from django.urls import path
app_name = 'userauth'
urlpatterns = [
    path('newuser/', views.newuser, name="newuser"),
    path('login/', views.login_view, name="login"),
    path("", views.index, name='dash'),
    path('logout/', views.logout_view, name="logout"),
]
