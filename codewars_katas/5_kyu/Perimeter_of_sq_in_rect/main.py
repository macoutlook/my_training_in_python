def perimeter(n):
    prev, next = 1, 1
    sum = prev + next
    counter = 2
    while counter <= n:
        prev, next = next, prev+next
        sum += next
        counter += 1
    return 4 * sum


def main():
    print perimeter(1000000)

if __name__ == '__main__':
    main()