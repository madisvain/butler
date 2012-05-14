#coding: utf-8

import random
import string

''' A random password generator
'''
def make_password(length=10, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for x in range(length))