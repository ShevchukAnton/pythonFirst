import sys
from hashlib import sha3_512

from .DBService import Accounts

FULL_SOURCE = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_')
ALPHABET_SOURCE = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
SECRET = 'Mega_Secret-salt'


def get_hex(salt, passw):
    salt = salt.encode('utf-8')
    passw = passw.encode('utf-8')
    return sha3_512(salt + passw).hexdigest()


def make_pass(resource_name, plain_pass):
    salt = get_hex(SECRET, resource_name)
    hash = get_hex(salt, plain_pass)
    return ''.join(get_hex(salt, hash))


def generate_pass(resource_name, plain_pass, pass_length=23, use_symbols=True):
    assert int(pass_length) > 8, 'Password length can\'t be less than 8 symbols'
    if str(use_symbols).lower() in ('true', 'y', 'yes'):
        alphabet = FULL_SOURCE
    else:
        use_symbols = False
        alphabet = ALPHABET_SOURCE

    rez = make_pass(resource_name, plain_pass)

    num = int(rez, 16)
    num_chars = len(alphabet)
    passwd = []
    while len(passwd) < int(pass_length):
        num, idx = divmod(num, num_chars)
        passwd.append(alphabet[idx])

    Accounts.create(name=resource_name, length=pass_length, p_hash=rez, symbols=use_symbols)

    print('Final pass - ' + ''.join(passwd))


def run(args):
    if len(args) == 5:
        generate_pass(args[1], args[2], args[3], args[4])
    elif len(args) == 4:
        generate_pass(args[1], args[2], args[3])
    else:
        generate_pass(args[1], args[2])


# first arg - resource for which password will be generated
# second arg - some password that u would like to use to generate new one. Master password actually
# third arg - how long generated pass should be (optional), 23 by default
# fourth arg - use special symbol or not (optional), True by default
if __name__ == "__main__":
    run(sys.argv)
