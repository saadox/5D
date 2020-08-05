

imps = __import__('__configs__.glob', fromlist=['PATHS']).PATHS
print(imps.FILE(__file__))

