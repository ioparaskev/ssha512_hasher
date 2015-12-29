# This is a porting of https://gist.github.com/garrettreid/8329796
# to Python 3 with some more additions (time compare, dialogs etc)
# for Python 2.x use the above gist

from hashlib import sha512
import os
import base64
from hmac import compare_digest as constant_time_compare


class SSHA512Hasher(object):

    def __init__(self, salt=os.urandom(16)):
        self.salt = salt

    def encode(self, password, salt=None):
        assert password is not None
        if not salt:
            salt = self.salt
        sha = sha512()
        password = password.encode('utf-8')
        sha.update(password)
        sha.update(salt)
        ssha512 = base64.b64encode(sha.digest() + salt)

        return "{}".format(ssha512.decode('utf-8'))

    def verify(self, password, encoded, stripped=None):
        try:
            salt = self.extract_salt(stripped or encoded)
        except RuntimeError as err:
            print('An error occured: {0}'.format(err))
            return False

        encoded_2 = self.encode(password, salt)
        return constant_time_compare(encoded, encoded_2)

    @staticmethod
    def extract_salt(striped):
        try:
            decoded = base64.b64decode(striped)
            # we don't care how big salt is. everything after 64 is salt
            salt = decoded[64::]
        except Exception as err:
            raise RuntimeError('An exception was raised: {0}'.format(err))
        return salt


class DovecotSSHA512Hasher(SSHA512Hasher):
    def encode(self, password, salt=None):
        hashed = super(DovecotSSHA512Hasher, self).encode(password, salt)
        # Print it out with a prefix for Dovecot compatibility
        return "{{SSHA512}}{}".format(hashed)

    def verify(self, password, encoded, stripped=None):
        stripped = encoded.replace('{SSHA512}', '')
        return super(DovecotSSHA512Hasher, self).verify(password, encoded,
                                                        stripped)


def setup_hasher(hasher_type):
    if hasher_type is 'a':
        hasher = SSHA512Hasher()
    elif hasher_type is 'b':
        hasher = DovecotSSHA512Hasher()
    else:
        raise RuntimeError
    return hasher


def verify_password(hasher):
    input_print = 'Enter the hash'
    if isinstance(hasher, DovecotSSHA512Hasher):
        input_print = '{0} with the {{SSHA512}} prefix'.format(input_print)
    input_print = '{0}:\n'.format(input_print)

    dovhash = input(input_print)
    if hasher.verify(passwd, dovhash):
        print("It's a match!")
    else:
        print("Pass doesn't match the hash!")


if __name__ == '__main__':
    hash_type = input('Enter [a] for simple SSHA512, [b] for dovecot '
                      'compatibility\n')

    shahasher = setup_hasher(hash_type)

    choice = input('Enter [a] for encode\n[b] for decode:\n')
    passwd = input('Enter a password:\n')
    if choice is 'a':
        print(shahasher.encode(passwd))
    elif choice is 'b':
        verify_password(shahasher)
    else:
        print('You entered an incorrect option!\nExiting......')
        exit(1)
