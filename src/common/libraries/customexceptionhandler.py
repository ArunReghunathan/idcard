
__author__ = ["Arun Reghunathan"]

import logging

from django.http.response import Http404
from rest_framework import status
from rest_framework.status import is_client_error
from src.common.libraries.customexceptions import BaseCustomException
from src.common.libraries.customresponse import CustomResponse

logger = logging.getLogger('wolfe')


def get_message(exc):
    message = getattr(exc, 'message', None)
    if not message:
        message = getattr(exc, 'detail', "Unhandled Exception")
    return message


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django Rest Framework that adds
    the `status_code` to the response and renames the `detail` key to `error`.
    """

    import traceback
    stack = traceback.format_exc()
    logger.exception(stack)

    if exc.__class__.__name__ == 'DoesNotExist':
        code = status.HTTP_404_NOT_FOUND
        message = get_message(exc)

    elif exc.__class__.__name__ == 'Http404':
        code = status.HTTP_404_NOT_FOUND
        message = "Resource Not Found"

    elif exc.__class__.__name__ in ['KeyError', 'MultiValueDictKeyError', 'AttributeError']:
        code = status.HTTP_400_BAD_REQUEST
        message = 'Bad request must pass: {}'.format(get_message(exc))

    elif exc.__class__.__name__ == 'ValidationError':
        code = status.HTTP_400_BAD_REQUEST
        message = get_message(exc)

    elif exc.__class__.__name__ == 'IntegrityError':
        code = status.HTTP_400_BAD_REQUEST
        message = exc[1]

    elif exc.__class__.__name__ == 'error':
        code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = get_message(exc)

    elif hasattr(exc, 'code') and is_client_error(exc.code) and isinstance(exc, BaseCustomException):
        code = exc.code
        message = get_message(exc)

    else:
        code = status.HTTP_500_INTERNAL_SERVER_ERROR
        message = get_message(exc)

    app_version = getattr(context['request'], 'app_version', None)

    response = CustomResponse(
        message=message,
        etype=exc.__class__.__name__,
        status=code,
        app_version=app_version,
        content_type='application/json'
    )
    return response
