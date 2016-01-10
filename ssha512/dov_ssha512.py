# This is a porting of https://gist.github.com/garrettreid/8329796
# to Python 3 with some more additions (time compare, dialogs etc)
# for Python 2.x use the above gist

from . import ssha512


class DovecotSSHA512Hasher(ssha512.SSHA512Hasher):
    def __init__(self):
        super(DovecotSSHA512Hasher, self).__init__(prefix='{SSHA512}')
