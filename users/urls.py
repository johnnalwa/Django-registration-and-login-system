
from django.urls import path
from . import views
from .views import home  # Import specific views


urlpatterns = [
    path('', home, name='users-home'),
    path('register/', views.RegisterView.as_view(), name='users-register'),
    path('profile/', views.profile, name='users-profile'),

]
