from django.urls import path
from . import views

app_name = "chai"
urlpatterns = [
    path("", views.all_chai, name="all_chai"), # /chai/
]