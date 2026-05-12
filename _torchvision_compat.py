"""Compatibility helpers for newer torchvision releases.

BasicSR 1.4.2 still imports ``torchvision.transforms.functional_tensor``.
Recent torchvision releases moved ``rgb_to_grayscale`` to
``torchvision.transforms.functional``. This shim recreates the old module path
so downstream imports keep working without patching site-packages.
"""

from __future__ import annotations

import sys
import types


def ensure_torchvision_functional_tensor() -> None:
    """Expose ``functional_tensor.rgb_to_grayscale`` on newer torchvision."""
    if 'torchvision.transforms.functional_tensor' in sys.modules:
        return

    try:
        from torchvision.transforms.functional_tensor import rgb_to_grayscale  # type: ignore
    except ImportError:
        try:
            from torchvision.transforms.functional import rgb_to_grayscale
        except ImportError:
            return

        functional_tensor = types.ModuleType('torchvision.transforms.functional_tensor')
        functional_tensor.rgb_to_grayscale = rgb_to_grayscale
        sys.modules['torchvision.transforms.functional_tensor'] = functional_tensor


__all__ = ['ensure_torchvision_functional_tensor']
