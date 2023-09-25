
from django.urls import path
from . import views

urlpatterns = [
    path('api/predict/', views.HtmlFileView.as_view(), name="odder"),
]
