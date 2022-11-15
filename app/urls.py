
from django.urls import path
from . import views

urlpatterns = [
    path('api/<int:first>/<int:second>', views.OdderView.as_view()),
    path('pretty/<int:first>/<int:second>', views.PrettyView.as_view())
]
