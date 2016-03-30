
def chain(*iterables):
    '''
    Make an iterator that returns elements from the first iterable until it is exhausted,
    then proceeds to the next iterable, until all of the iterables are exhausted

    >>> list(chain('ABC', 'DEF'))
    ['A', 'B', 'C', 'D', 'E', 'F']

    >>> list(chain([1, 2, 3], [4, 5, 6]))
    [1, 2, 3, 4, 5, 6]
    '''



def count(start=0, step=1):
    '''
    Make an iterator that returns evenly spaced values starting with n.
    (Caution! it's infinite sequence)

    >>> c = count(10)
    >>> c.next(); c.next(); c.next()
    10
    11
    12

    >>> zip(count(1), 'string')
    [(1, 's'), (2, 't'), (3, 'r'), (4, 'i'), (5, 'n'), (6, 'g')]
    '''




def ifilter(predicate, iterable):
    '''
    Make an iterator that filters elements from iterable returning
    only those for which the predicate is True

    >>> list(ifilter(lambda x: x % 2, range(10)))
    [1, 3, 5, 7, 9]
    '''
            
