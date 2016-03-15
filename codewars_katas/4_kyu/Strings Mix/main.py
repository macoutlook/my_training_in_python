from itertools import groupby
def mix(s1, s2):
    lst_s1, lst_s2 = [], []
    res = ''
    for k, g in groupby(sorted(s1)):
        tmp = list(g)
        tmp.insert(0, 1)
        if len(tmp) > 2 and tmp[1].islower():
            lst_s1.append(tmp)
    for k, g in groupby(sorted(s2)):
        tmp = list(g)
        tmp.insert(0, 2)
        if len(tmp) > 2 and tmp[1].islower():
            ind = [ind for ind, el in enumerate(lst_s1) if tmp[1] in el]
            if not ind:
                lst_s2.append(tmp)
            elif len(lst_s1[ind[0]]) == len(tmp):
                tmp[0]+= 1
                lst_s2.append(tmp)
                lst_s1.remove(lst_s1[ind[0]])
            elif len(lst_s1[ind[0]]) < len(tmp):
                lst_s2.append(tmp)
                lst_s1.remove(lst_s1[ind[0]])
    lst = lst_s1 + lst_s2
    print lst
    lst.sort(key=lambda x: x[1:])
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: len(x), reverse=True)
    print lst
    for el in lst:
        if el[0] ==3:
            res = res + "=:" + ''.join(el[1:])
        else:
            res = res + str(el[0]) + ":" + ''.join(el[1:])
        if not el == lst[-1]:
            res = res + "/"
    return res




def main():
    print mix("Are they here", "yes, they are here")


if __name__ == '__main__':
    main()