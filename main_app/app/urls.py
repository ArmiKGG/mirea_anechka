
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('api/<int:first>/<int:second>', views.OdderView.as_view(), name="odder"),
    path('pretty/<int:first>/<int:second>', views.PrettyView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path("docs/", SpectacularSwaggerView.as_view(
        url_name="schema"
    ),
         name="swagger-ui")
]
