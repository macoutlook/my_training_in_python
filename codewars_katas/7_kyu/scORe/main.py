from multiprocessing.pool import ThreadPool


def yield_el(n):
    return (x for x in xrange(n+1))


def count_sum(n):
    sum_of_bin = 0
    for x in yield_el(n):
        sum_of_bin = x | sum_of_bin
    return sum_of_bin


def score(n):
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(count_sum, (n,))
    sum_of_bin = async_result.get()
    return sum_of_bin


def main():
    print score(49)

if __name__ == '__main__':
    main()