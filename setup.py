import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SSHA512Hasher",
    version="0.5",
    author="John Paraskevopoulos",
    author_email="ioparaskev@gmail.com",
    description="Simple SSHA512 hasher with Dovecot format support",
    license="GPL-3.0",
    url="https://github.com/ioparaskev/ssha512_hasher",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or "
        "later (GPLv3+)",
    ],
)