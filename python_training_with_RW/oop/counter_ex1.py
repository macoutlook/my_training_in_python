
class CallCounter(object):
    '''
    Decorator for counting number of function calls
    
    >>> @CallCounter
    ... def f(x, y, z=1):
    ...     return x+y*z
    ... 
    >>> f(2, 4, 6)
    26
    >>> f(3, 5, 7)
    38
    >>> f(8, 2)
    10
    >>> CallCounter.counter
    3
    '''
    counter = 0

    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        CallCounter.counter += 1
        return self.func(*args, **kwargs)



@CallCounter
def f(x, y, z=1):
    return x+y*z


f(2,3,4)
f(1,2,3)
print CallCounter.counter


