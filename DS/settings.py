from .base_settings import *


try:
    from .local_settings import *
except ImportError:
    from .prod_settings import *

