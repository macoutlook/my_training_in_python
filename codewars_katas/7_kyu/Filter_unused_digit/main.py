def unused_digits(*args):
    main_tup = '0123456789'

    for _, number in enumerate(args):
        for digit in str(number):
            if digit in main_tup:
                main_tup = main_tup.replace(digit, "")

    return str(main_tup)


def main():
    res = unused_digits(12, 34, 56, 78)
    print res

if __name__ == '__main__':
    main()