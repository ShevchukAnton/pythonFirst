def myfunc(*args):
    """ * handle argument as a list of values, args stays for arguments"""
    for a in args:
        print(a, end = '  ')
    if args:
        print()


def myfunc2(**kwargs):
    """ ** handle argument as an dictionary with keywords, so kwargs stays for keyword arguments"""
    for k, v in kwargs.items():
        print(k, v, sep = ' => ', end = '\n')
    if kwargs:
        print()


myfunc(1, 2, 3, 4, 5, 6, 7, 'sdfa')
print('+++++++++++++++++++++++\n')
myfunc2(values = 123, burg = 'cheese')
print('+++++++++++++++++++++++\n')


def myfunc3(*args, **kwargs):
    """This function accepts any amount of arguments of any types, including list of key/value pairs"""
    if args:
        for a in args:
            print(a, end = '  ')
        print()
    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep = ' => ', end = '\n')
        print()


myfunc3(1, 2, 3, 4, 5, 6, 7, 'sdfa', cusValue = 123243, beware = True)
