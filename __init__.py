"""Top-level package for test-extension."""

from .src.test_extension.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """Max Klein"""
__email__ = "you@example.com"
__version__ = "0.0.1"


WEB_DIRECTORY = "./web"
