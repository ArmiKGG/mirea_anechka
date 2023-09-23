
from django.urls import path
from . import views

urlpatterns = [
    path('api/file/', views.HtmlFileView.as_view(), name="odder"),
]
