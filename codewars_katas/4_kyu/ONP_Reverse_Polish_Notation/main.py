import operator


def calc(expr):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div,
    }
    stack = []
    if not expr: stack.append(0)
    else:
        for el in expr.split(' '):
            try:
                stack.append(float(el))
            except:
                a = stack.pop()
                b = stack.pop()
                stack.append(opers[el](b, a))
    return stack[-1]

# arti
def calc(expr):
    stack = []
    for element in expr.split():
        if all(e.isdigit() or e == '.' for e in element):
            stack.append(float(element))
        else:
            a, b = stack.pop(), stack.pop()
            if element == '+':
                stack.append(b+a)
            elif element == "-":
                stack.append(b-a)
            elif element == "*":
                stack.append(b*a)
            elif element == "/":
                stack.append(b/a)
    if stack:
        res = stack.pop()
    else:
        res = 0
    return res


def main():
    print calc("5")


if __name__ == '__main__':
    main()