import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SSHA512_hasher",
    version="0.5",
    author="John Paraskevopoulos",
    author_email="ioparaskev@gmail.com",
    description="Simple SSHA512 hasher with Dovecot format support",
    license="GPL-3.0",
    url="https://github.com/ioparaskev/ssha512_hasher",
    packages=['ssha512'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: GPL-3.0 License",
    ],
)