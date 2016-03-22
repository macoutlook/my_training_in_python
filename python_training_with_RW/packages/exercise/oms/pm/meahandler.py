from ..fm import fmadapter as fm

def is_python_2():
    return fm.python_line() == 2

if __name__ == '__main__':
    print is_python_2()
    
