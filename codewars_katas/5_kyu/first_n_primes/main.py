import math
from itertools import count


class Primes:

    @staticmethod
    def first(n):
        el = 3
        ret_set = set()
        ret_set.add(2)

        for el in count(3, 2):
            if len(ret_set) == n:
                return sorted(list(ret_set))
            if all(el % i for i in xrange(3, int(math.sqrt(el))+1, 2)):
                ret_set.add(el)


        # while counter != n:
        #     if all(el % i for i in xrange(3, int(math.sqrt(el))+1, 2)):
        #         ret_set.add(el)
        #         counter += 1
        #     el += 2
        # return sorted(list(ret_set))

    @staticmethod
    def is_prime(el):
        for div in xrange(2, int(el ** 0.5)+1):
            print ":el:%s div:%s" %(el, div)
            if el % div == 0:
                return False
        return True

    @staticmethod
    def is_prime_2(a):
        return all(a % i for i in xrange(2, a))


def main():
    print Primes.first(300)

if __name__ == '__main__':
    main()