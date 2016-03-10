def solution(digits):
    sum_of_frag = 0
    max_seq = '0'
    max = 0
    for ind, digit in enumerate(digits):
        if digit >= max:
            max = digit
            if int(digits[ind:ind+5]) > int(max_seq):
                max_seq = digits[ind:ind+5]

    return max_seq


def main():
    print solution('1234567898765')

if __name__ == '__main__':
    main()