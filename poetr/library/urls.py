from django.urls import path
from .views import Page, Random

urlpatterns = [
    path('<int:pk>/', Page.as_view(), name="Page"),
    path('', Random, name="Random")
]