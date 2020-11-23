from .settings import *

if DEBUG:
    def show_toolbar(request):
        return True
    
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    LOGGING = {
        'version' : 1,
        'disable_existing_loggers' : False,
        
        'loggers' : {
            'django' : {
                'handlers' : ['console'],
                'level' : 'INFO',
            },
            'app' : {
                'handlers' : ['console'],
                'level' : 'INFO',
            }
        },
        'handlers' : {
            'console' : {
                'level' : 'INFO',
                'class' : 'logging.StreamHandler',
                'formatter' : 'dev',
            },
            'file' : {
                'level' : 'INFO',
                'class' : 'logging.handlers.TimedRotatingFileHandler',
                'filename' : os.path.join(BASE_DIR, 'logs/django.log'),
                'when' : 'D',
                'interval' : 1,
                'backupCount' : 7,
                'formatter' : 'dev',
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'formatter': 'dev',
            },
        },
        'formatters' : {
            'dev' : {
                'format' : '\t'.join([
                    '%(asctime)s',
                    '[%(levelname)s]',
                    '%(pathname)s(Line:%(lineno)d)',
                    '%(message)s',
                ]),
            },
        },
    }

