#coding: utf-8

import random
import string
from time import time, localtime, strftime

from fabric.api import env
from fabric.colors import white


''' A random password generator
'''
def make_password(length=10, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for x in range(length))

''' Calculates a delta from the start_time
'''
def delta(start_time):
    return str(round((time() - start_time), 2))

''' Prints a timed message
'''
def message(message, start_time=time(), color=white):
    d = delta(env.start_time)
    print(strftime("%H:%M:%S", localtime()) + '\t' + d + '\t' + color(message))
