

import os


class AppConfig(object):
    DEBUG = True
    SITE_NAME = os.environ.get('FD_SITE_NAME', 'Flask Community')
    SECRET_KEY = os.environ.get('FD_SECRET_KEY', 'ThisIsJustTheDevKey')
    SQLALCHEMY_DATABASE_URI = os.environ.get('FD_SQLA_URI', 'sqlite:///fd.db')
    DEBUG_TB_INTERCEPT_REDIRECTS = False
