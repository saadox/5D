from os import path
# this is gpo where I will be storing GLOBAL PURPOSES OBJECTS to use them

FILE = lambda f_name: path.abspath(path.realpath(f_name))
DIR  = lambda f_name: path.dirname(path.realpath(f_name))