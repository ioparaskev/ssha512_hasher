from ssha512.dov_ssha512 import DovecotSSHA512Hasher
from ssha512.ssha512 import SSHA512Hasher


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
    wrong_option = 'You entered an incorrect option!\nExiting......'

    try:
        shahasher = setup_hasher(hash_type)
    except RuntimeError:
        print(wrong_option)
        exit(1)

    choice = input('Enter [a] for encode\n[b] for decode:\n')
    passwd = input('Enter a password:\n')
    if choice is 'a':
        print(shahasher.encode(passwd))
    elif choice is 'b':
        verify_password(shahasher)
    else:
        print(wrong_option)
        exit(1)
