

# imps = __import__('__configs__.glob', fromlist=['PATHS']).PATHS
# print(imps.FILE(__file__))

from  __core__.LEX3R.lex import Lexer

try :
    Lx = Lexer('test.lang')
    tokens = Lx.start()

    print(tokens)
except Exception as ex:
    print("Exception happend 0_0 !\n-> "+str(ex))

