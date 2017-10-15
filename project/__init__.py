from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .worker import worker as celery_app
from .tasks import *

# from src.common.libraries.paymentlib import capture_all

__all__ = ['celery_app']