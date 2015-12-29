# This is a porting of https://gist.github.com/garrettreid/8329796
# to Python 3 with some more additions (time compare, dialogs etc)
# for Python 2.x use the above gist

import ssha512.ssha512 as ssha512
from os import urandom


class DovecotSSHA512Hasher(ssha512.SSHA512Hasher):
    def __init__(self, salt=urandom(16)):
        super(DovecotSSHA512Hasher, self).__init__(salt=salt,
                                                   prefix='{{SSHA512}}')
