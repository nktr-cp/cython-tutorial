from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("py_version_hex.pyx", annotate=False)
)

