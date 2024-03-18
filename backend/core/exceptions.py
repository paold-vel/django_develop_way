from django.core.exceptions import PermissionDenied
from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def base_exception_handler(exc: Exception, context: dict) -> Response:
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response_data = None
    if isinstance(exc, APIException):
        response_data = {'detail': exc.detail, 'status': exc.status_code}
    response = exception_handler(exc, context)

    if response and response_data:
        response.data = response_data

    return response
