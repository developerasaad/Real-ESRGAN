# flake8: noqa
from _torchvision_compat import ensure_torchvision_functional_tensor

ensure_torchvision_functional_tensor()

from .archs import *
from .data import *
from .models import *
from .utils import *

try:
    from .version import *
except ImportError:
    pass
