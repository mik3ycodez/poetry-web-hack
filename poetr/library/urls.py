from django.urls import path
from .views import Page, Random, NewPoem, NewReport

urlpatterns = [
    path('<int:pk>/', Page.as_view(), name="Page"),
    path('<int:pk>/new/', NewPoem, name="new"),
    path('<int:pk>/report/', NewReport, name="report"),
    path('', Random, name="Random")
]