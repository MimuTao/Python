
class Iexception(Exception):
    pass

try:
    raise Iexception('error')
except Iexception as exec:
    print(exec)
