'''
This does not work:

import urllib2
with urllib2.urlopen('http://www.python.org/') as conn:
    print len(conn.read())

Prepare class which will make such construction possible.
It should work like this:

with <Your class>('http://www.python.org/') as conn:
    print len(conn.read())

Connection should be closed after `with` statement    
'''
import urllib2

class UrlOpen(object):
    def __init__(self, url):
        self.url = url
        self.response = None

    def read(self):
        return self.response.read()

    def __enter__(self):
        self.response = urllib2.urlopen(self.url)
        return self.response

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.response.close()



def main():
    with UrlOpen('http://www.python.org/') as conn:
        print len(conn.read())


if __name__ == '__main__':
    main()

