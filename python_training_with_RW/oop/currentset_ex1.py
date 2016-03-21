
class Currentset(object):
    '''
    Create Currentset class with attributes: name, ip, description
    It should work like this:

    >>> cs = Currentset(*('Faraday;10.121.85.21;HPOMS-01'.split(';')))
    >>> cs
    name=Faraday,ip=10.121.85.21,description=HPOMS-01
    >>> [cs]
    [name=Faraday,ip=10.121.85.21,description=HPOMS-01]
    >>> print cs
    name=Faraday,ip=10.121.85.21,description=HPOMS-01
    '''
    def __init__(self, name, ip, description):
        self.name = name
        self.ip = ip
        self.description = description
        self.string = "name=%s,ip=%s,description=%s" % (self.name, self.ip, self.description) 

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

def main():
    cs = Currentset('Faraday','10.121.85.21','HPOMS-01')
    cs
    # print cs

if __name__ == '__main__':
    main()

    
