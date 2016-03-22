from oms.pm import meahandler

def main():
    if meahandler.is_python_2():
        print 'OK'
    else:
        print 'WRONG'


if __name__ == '__main__':
    main()
