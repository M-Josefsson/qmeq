"""
This QmeQ package contains modules, where different approximate master equations
are implemented. Modules starting with `c_` are implemented using Cython.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# For backwards compatibility with 1.0
import sys
from .base import pauli
from .base import lindblad
from .base import neumann1
from .base import neumann2
sys.modules['qmeq.approach.pauli'] = pauli
sys.modules['qmeq.approach.lindblad'] = lindblad
sys.modules['qmeq.approach.neumann1'] = neumann1
sys.modules['qmeq.approach.neumann2'] = neumann2

try:
    from .base import c_pauli
    from .base import c_lindblad
    from .base import c_neumann1
    from .base import c_neumann2
    sys.modules['qmeq.approach.c_pauli'] = pauli
    sys.modules['qmeq.approach.c_lindblad'] = lindblad
    sys.modules['qmeq.approach.c_neumann1'] = neumann1
    sys.modules['qmeq.approach.c_neumann2'] = neumann2
except ImportError:
    pass
