import operator


class Calculator(object):

    def evaluate(self, string):
        opers = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.div,
        }
        high_prior = r'/*'
        low_prior = r'+-'
        lst = string.split(" ")
        ind = 1
        while len(lst) > 1:
            if lst[ind] in high_prior:
                lst[ind-1] = opers[lst[ind]](float(lst[ind-1]), float(lst[ind+1]))
                lst.remove(lst[ind+1])
                lst.remove(lst[ind])
            elif not any(x in lst for x in high_prior) and any(x in lst for x in low_prior):
                ind = 1
                lst[ind-1] = opers[lst[ind]](float(lst[ind-1]), float(lst[ind+1]))
                lst.remove(lst[ind+1])
                lst.remove(lst[ind])
            else:
                ind += 2
        return round(float(lst[0]),3)


def main():
    calcObj = Calculator()
    print calcObj.evaluate("2 / 2 + 3 * 4 - 6")

if __name__ == '__main__':
    main()