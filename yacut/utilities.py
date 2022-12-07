import secrets
import string

from settings import DEFAULT_SHORT


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(DEFAULT_SHORT))
    return crypt_rand_string
