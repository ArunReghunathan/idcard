import logging

import logging
# from django.utils.decorators import decorator_from_middleware
# from .middleware import ExceptionMiddleware, RequestMiddleware

__author__ = ["Arun Reghunathan"]


class LoggingMixin(object):
    """
    Adds RequestLogMiddleware to any Django View by overriding as_view.
    """

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super(LoggingMixin, cls).as_view(*args, **kwargs)
        # view = decorator_from_middleware(RequestMiddleware)(view)
        # view = decorator_from_middleware(ExceptionMiddleware)(view)
        return view
