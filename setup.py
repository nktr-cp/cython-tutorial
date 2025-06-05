from setuptools import setup
from Cython.Build import cythonize

setup(
    # ext_modules = cythonize("hello_world.py")
    # ext_modules = cythonize("primes.pyx")
    ext_modules = cythonize("primes.py")
)

