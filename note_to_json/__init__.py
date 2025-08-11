# note_to_json/__init__.py
from importlib.metadata import PackageNotFoundError, version as _pkg_version

__all__ = ["__version__"]

try:
    __version__ = _pkg_version("note-to-json")
except PackageNotFoundError:
    # Running from a checkout / not installed
    __version__ = "0+unknown"
