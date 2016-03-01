def strong_enough( earthquake, age ):
    beg_strength = 1000.0
    result = "Safe"

    for _ in xrange(age):
        beg_strength = beg_strength - (0.01 * beg_strength)

    magnitude = sum(earthquake[0])*sum(earthquake[1])*sum(earthquake[2])

    if beg_strength < magnitude:
        result = "Needs Reinforcement!"
    return result


def main():
    res = strong_enough([[2,3,1],[3,1,1],[1,1,2]], 2)
    print res

if __name__ == '__main__':
    main()