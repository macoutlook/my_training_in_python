def next_bigger(n):
    n_tab = list("".join(str(n)))[::-1]
    print n_tab
    print sorted(''.join(n_tab))
    ind = 0
    if n >= int(''.join(sorted((n_tab), reverse=True))):
        return -1
    while True:

        if n_tab[ind] > n_tab[ind + 1]:
            smallest_right = min([dig for dig in n_tab[0:ind + 1] if dig > n_tab[ind+1]])
            left = n_tab[ind + 2:][::-1]
            div = n_tab[ind+1]
            right = n_tab[0: ind + 1][::-1]
            left.append(smallest_right)
            right.append(div)
            del right[right.index(smallest_right)]
            return int("".join(left + sorted(right)))
        ind += 1

# szuka powtorzen w sekwencji i wypieprza powtorzenia
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def main():
    print next_bigger(2111)

    # 7 1 0 2


if __name__ == '__main__':
    main()