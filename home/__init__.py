from os import path
from django.apps import AppConfig

#修改app应用名称
VERBOSE_NAME = u"高校本表单管理"

def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]

class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_NAME

default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
