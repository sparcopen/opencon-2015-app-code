"""
Import fabric modules.
"""
from __future__ import absolute_import

import django
django.setup()

from . import play
from . import ops
from . import repair
