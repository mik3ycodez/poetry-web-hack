from django.urls import path
from .views import Page, Random, NewPoem

urlpatterns = [
    path('<int:pk>/', Page.as_view(), name="Page"),
    path('<int:pk>/new/', NewPoem.as_view(), name="new"),
    path('', Random, name="Random")
]