"""Top-level package for test-extension."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """Robin Huang"""
__email__ = "robin@drip.art"
__version__ = "0.0.1"

from .src.test_extension.nodes import NODE_CLASS_MAPPINGS
from .src.test_extension.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
