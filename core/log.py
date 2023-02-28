import datetime
import logging.config
import os

from core.config import settings

LOG_PATH = os.path.join(settings.BASE_DIR, 'logs')
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)
LOGGING = {
    # 必须是1
    'version': 1,
    # 默认为True，禁用日志
    'disable_existing_loggers': False,
    # 定义formatters组件，定义存储日志中的格式
    'formatters': {
        'default': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]:%(message)s'
        }
    },
    # 定义loggers组件，用于接收日志信息
    # 并且将日志信息丢给handlers去处理
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    },
    # 定义handlers组件，用户写入日志信息
    'handlers': {
        'console': {
            'level': 'INFO',
            # 定义存储日志的文件
            'filename': f'{LOG_PATH}/{datetime.datetime.now().strftime("%Y_%m_%d")}_api.log',
            # 指定写入日志中信息的格式
            'formatter': 'default',
            # 指定日志文件超过5M就自动做备份
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 5 * 1024 * 1024,
        }
    }
}
logging.config.dictConfig(LOGGING)
log = logging.getLogger('console')
