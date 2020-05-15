from distutils.core import setup
from distutils.extension import Extension
cmatrixmodule = Extension(name="example", sources=['example.c', ])
setup(name="example", ext_modules=[cmatrixmodule])
