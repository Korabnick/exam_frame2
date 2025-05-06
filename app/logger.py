import logging
import json
from logging.config import dictConfig
from flask import request

def configure_logging(app):
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
            'json': {
                '()': 'app.logger.JsonFormatter',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter': 'default'
            },
            'json': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
                'formatter': 'json'
            }
        },
        'root': {
            'level': app.config['LOG_LEVEL'],
            'handlers': ['console'] if app.config['FLASK_ENV'] == 'development' else ['json']
        }
    })

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        if hasattr(request, 'url'):
            log_record.update({
                'url': request.url,
                'method': request.method,
                'remote_addr': request.remote_addr,
            })
        
        return json.dumps(log_record)