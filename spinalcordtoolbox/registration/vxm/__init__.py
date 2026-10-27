"""
Vendored subset of VoxelMorph 0.2 (PyTorch backend), used by `algo=dl` registration.

Only the code needed to build `VxmDense` is included, so that SCT doesn't depend on the
`voxelmorph`, `neurite`, and `pystrum` packages. See: https://github.com/spinalcordtoolbox/spinalcordtoolbox/issues/4899
"""

from . import layers
from . import networks

__all__ = ["layers", "networks"]
