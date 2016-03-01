from types import IntType, LongType, FloatType


def foo(a,b):
    my_types_tup = (IntType, LongType, FloatType)
    if not (type(a) in my_types_tup) or not (type(b) in my_types_tup):
        return False
    elif (type(a) in my_types_tup) and (type(b) in my_types_tup):
        return (a % b) + (b % a)


def main():
    res = foo(2, "sss")
    print res

if __name__ == '__main__':
    main()