def decorator_func1(func):
    def newfunc(*args):
        print("Func decorator_func1:")
        print("Args are:",args)
        return func(*args)
    return newfunc

def decorator_func2(func):
    def newfunc(*args):
        print("Func decorator_func2")
        print("Args are:",args)
        return func(*args)
    return newfunc

@decorator_func1
@decorator_func2
def isum(*args):
    return sum(args)
#
# print(isum(1,2,3,4))
# print(isum.__name__)



print(isum(1,2,3,4,5,6,7,8,9))
