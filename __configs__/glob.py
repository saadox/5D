__import__('sys').path.append('..') # to get rid of Beyond Top-lvl import.

TEST_MODE = True
PATHS     = __import__('__imports__.gpo', fromlist=['FILE', 'DIR'])
