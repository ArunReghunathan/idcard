import os

if os.environ.get('PYTHONENV') in ['PROD', 'STAGING']:
    LOG_DIR = '/opt/production-logs/'
else:
    LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {

        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'fmt': '%(levelname)s %(asctime)s %(message)s',
        },

        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s'
                      ' %(name)s %(module)s %(funcName)s %(lineno)d '
                      '%(process)d %(thread)d %(message)s'
        },
        'json_verbose': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'format': '%(levelname)s %(asctime)s'
                      ' %(name)s %(module)s %(funcName)s %(lineno)d '
                      '%(process)d %(thread)d %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        },
    },

    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'wolfe_file': {
            'level': 'INFO',
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'wolfe.log'),
            'when': 'D',
            'interval': 1
        },

        'request_file': {
            'level': 'INFO',
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'requests.log'),
            'when': 'D',
            'interval': 1
        },

        'worker_file': {
            'level': 'INFO',
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'worker.log'),
            'when': 'D',
            'interval': 1
        },

        'notification_file': {
            'level': 'INFO',
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'notification.log'),
            'when': 'D',
            'interval': 1
        },

        'other_file': {
            'level': 'INFO',
            'formatter': 'json',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'other.log'),
            'when': 'D',
            'interval': 1
        },

        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            # 'class': 'logutils.colorize.ColorizingStreamHandler',
            'formatter': 'verbose'
            # 'formatter': 'simple'
        },
    },

    'loggers': {
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['wolfe_file', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },

        'wolfe': {
            'handlers': ['wolfe_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },

        'requests': {
            'handlers': ['request_file', 'console'],
            'level': 'INFO',
            'propagate': True,

        },

        'worker': {
            'handlers': ['worker_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },

        'other': {
            'handlers': ['other_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'notification': {
            'handlers': ['notification_file', 'console'],
            'level': 'INFO',
            'propagate': True,
        }

    }
}
