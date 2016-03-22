import sys, os
sys.path.append(os.path.abspath(os.path.split(os.path.dirname(__file__))[0]))
from oms.pm import meahandler


if meahandler.is_python_2():
    print 'OK'
else:
    print 'WRONG'
