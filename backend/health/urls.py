from django.urls import path

from backend.health.views import HealthCheckBackendView

app_name = 'health'

urlpatterns = [
    path('backend', HealthCheckBackendView.as_view(), name='health_backend_view'),
]
