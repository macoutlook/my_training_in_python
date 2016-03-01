from types import IntType, LongType, FloatType


def foo(a,b):
    if not (type(a) in (IntType, LongType, FloatType)) or not (type(b) in (IntType, LongType, FloatType)):
        return False
    elif (type(a) in (IntType, LongType, FloatType)) and (type(b) in (IntType, LongType, FloatType)):
        return (a % b) + (b % a)


def main():
    res = foo(2, "sss")
    print res

if __name__ == '__main__':
    main()