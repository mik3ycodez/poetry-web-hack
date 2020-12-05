from django.urls import path
from .views import Page

urlpatterns = [
    path('<int:pk>/', Page.as_view(), name="Page")
]