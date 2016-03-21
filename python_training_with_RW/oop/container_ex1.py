
'''
Implement container protocol/interface in classes `DataSource` and `Data`
in order to make function `load` working.
Container protocol requires following methods:
__contains__(self, item),
__setitem__(self, key, value),
__getitem__(self, key) 
'''

UNKNOWN, MEMORY, FILE, NETWORK = range(0, 4)
DATA = 'data'


class DataSource(object):
    def __init__(self):
        self._src = {MEMORY: Memory(), FILE: File(), NETWORK: Network()}

    def __contains__(self, item):
        if item in self._src:
            return True
        else:
            return False

    def __getitem__(self, key):
        return self._src[key]

    def __setitem__(self, key, value):
        raise TypeError("'DataSource' object is read-only")


class Data(object):
    def __init__(self, data):
        self._data = data

    def __contains__(self, item):
        if item in self._data:
            return True
        else:
            return False

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        raise TypeError("'Data' object is read-only")


class Memory(Data):
    def __init__(self):
        Data.__init__(self, {DATA: 'Memory data'})


class File(Data):
    def __init__(self):
        Data.__init__(self, {DATA: 'File data'})


class Network(Data):
    def __init__(self):
        Data.__init__(self, {DATA: 'Network data'})



def load(type, source):
    '''
    Load `Data` from `DataSource`
    
    >>> dataSrc = DataSource()
    >>> load(MEMORY, dataSrc)
    'Memory data... loaded'
    >>> load(FILE, dataSrc)
    'File data... loaded'
    >>> load(NETWORK, dataSrc)
    'Network data... loaded'
    >>> load(UNKNOWN, dataSrc)
    Traceback (most recent call last):
    [...]
    TypeError: 'DataSource' object is read-only
    '''
    if type in source:
        dataObj = source[type]
        if DATA in dataObj:
            item = dataObj[DATA]
            item += '... loaded'
            return item
    else:
        source[3] = {DATA: 'other data'}


def main():
    dataSrc = DataSource()
    load(MEMORY, dataSrc)
    load(FILE, dataSrc)
    load(NETWORK, dataSrc)
    load(UNKNOWN, dataSrc)


if __name__ == '__main__':
    main()
    
