from typing import Any

from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckBackendView(APIView):
    authentication_classes: tuple[Any, ...] = ()
    permission_classes: tuple[Any, ...] = ()

    def get(self, *args: Any, **kwargs: Any) -> Response:
        """
        Health check server
        """
        return Response('OK')
