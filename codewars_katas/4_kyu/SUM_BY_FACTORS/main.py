import operator

def prime_factors(n):
    n = abs(n)
    prime_factor = []
    divisor = 2
    max_divisor = (n + 1)
    while n != 1:
        for el in xrange(divisor, max_divisor):
            if (lambda el, n: el if n % el == 0 else False)(el, n):
                divisor = el
                prime_factor.append(divisor)
                n /= divisor
                break
    return prime_factor

def sum_for_list(lst):
    result = []
    lst_with_primes = map(prime_factors, lst)
    print lst_with_primes
    set_with_primes = set((item for sublist in lst_with_primes for item in sublist))
    for el in set_with_primes:
        lst_loc = []
        lst_loc.append(el)
        lst_loc.append(sum((numb for ind, numb in enumerate(lst) if el in lst_with_primes[ind])))
        result.append(lst_loc)
    return sorted(result, key = operator.itemgetter(0))

# Arczi solution
# def get_prime_factors_for_number(number):
#     res = set()
#     _factor = 2
#     tmp_val = number
#     while abs(number) >= _factor:
#         while not tmp_val % _factor:
#             tmp_val = tmp_val / _factor
#             res.add(_factor)
#         _factor += 1
#     return res
#
# def get_prime_factors_for_list(lst):
#     res = set()
#     for number in lst:
#         res.update(get_prime_factors_for_number(number))
#     return res
#
# def sum_for_list(lst):
#     print lst
#     factors = sorted(list(get_prime_factors_for_list(lst)))
#     res = [[x, sum(number for number in lst if not number % x)] for x in factors]
#     return res


def main():
    print sum_for_list([15, 21, 24, 30, -45])


if __name__ == '__main__':
    main()