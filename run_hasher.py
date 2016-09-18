from ssha512.dov_ssha512 import DovecotSSHA512Hasher
from ssha512.ssha512 import SSHA512Hasher
import sys

def bi_input(text):
    if sys.version_info[0] < 3:
        return raw_input(text)
    return input(text)

def setup_hasher(hasher_type):
    hasher = dict(a=SSHA512Hasher, b=DovecotSSHA512Hasher)
    return hasher[hasher_type]


def verify_password(word, hasher):
    input_print = 'Enter the hash'
    if isinstance(hasher, DovecotSSHA512Hasher):
        input_print = '{0} with the {{SSHA512}} prefix'.format(input_print)
    input_print = '{0}:\n'.format(input_print)

    cmp_hash = bi_input(input_print)
    if hasher.verify(word, cmp_hash):
        return "It's a match!"
    else:
        return "Pass doesn't match the hash!"

if __name__ == '__main__':
    hash_type = bi_input('Enter [a] for simple SSHA512, [b] for dovecot'
                         ' compatibility\n')
    choice = bi_input('Enter [a] for encode\n[b] for decode:\n')
    wrd = bi_input('Enter a string:\n')
    available_modes = dict(a=lambda word, hasher: hasher.encode(word),
                           b=lambda word, hasher: verify_password(word,
                                                                  sha_hasher))
    try:
        sha_hasher = setup_hasher(hash_type)()
        print(available_modes[choice](wrd, sha_hasher))
    except KeyError:
        print('You entered an incorrect option!\nExiting......')
        exit(1)
