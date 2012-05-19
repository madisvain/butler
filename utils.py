#coding: utf-8

import random
import string

from time import time


''' A random password generator
'''
def make_password(length=10, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for x in range(length))


def delta(start_time):
    return str(round((time() - start_time), 2))