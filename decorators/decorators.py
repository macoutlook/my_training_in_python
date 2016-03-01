
class MyDecorator(object):

    def __init__(self, func):
        print "inside constructor"
        func()

    def __call__(self):
        print "inside call"


def my_decor_func(func):
    def new_func():
        print "in new func"
        func()

    return new_func


@my_decor_func
def my_func():
    print "my func"


def main():
    print "end of my_func"

    my_func()

if __name__ == '__main__':
    main()