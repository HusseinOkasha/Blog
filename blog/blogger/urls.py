from django.urls import path
from .views import signup, home, login
urlpatterns = [
    path('signup/', signup),
    path('<int:id>/home/', home),
    path('login/', login),
]