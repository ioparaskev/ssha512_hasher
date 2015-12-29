from hmac import compare_digest as constant_time_compare
import base64
from hashlib import sha512
import os


class SSHA512Hasher(object):
    def __init__(self, salt=os.urandom(16), prefix=''):
        self.salt = salt
        self.prefix = prefix

    def encode(self, word, salt=None):
        if not word:
            raise RuntimeError('No word given to encode')
        if not salt:
            salt = self.salt
        sha = sha512()
        word = word.encode('utf-8')
        sha.update(word)
        sha.update(salt)
        ssha512 = base64.b64encode(sha.digest() + salt)

        return "{}{}".format(self.prefix, ssha512.decode('utf-8'))

    def verify(self, password, encoded):
        stripped = encoded.replace(self.prefix, '')
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
