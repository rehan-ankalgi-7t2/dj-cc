from django.urls import path
from . import views

app_name = "chai"
urlpatterns = [
    path("", views.all_chai, name="all_chai"), # /chai/
    path("<int:chai_id>/", views.chai_detail, name='chai_details'),
    path("chai_stores/", views.chai_store_view, name='chai_stores')
]