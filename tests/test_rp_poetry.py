"""
FastAPI Test application to serve models.
"""
from rp_poetry import __version__


def test_version():
    """
    Test the version of the package.
    """
    assert __version__ == "0.1.0"
