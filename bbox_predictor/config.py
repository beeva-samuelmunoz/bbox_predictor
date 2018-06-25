
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
SERVER_DEBUG = True


try:
    from .config_local import *
except:
    pass
