from django.urls import path
from . import views

urlpatterns = [
    path("helloworld/", views.hello_world, name="hello_world"),
    path("users/", views.users, name="users")
]
