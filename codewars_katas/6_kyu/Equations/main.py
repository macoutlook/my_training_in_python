import math
import math
def solution(n, m):
    result = 0
    max_sqrt = max([math.sqrt(n), math.sqrt(m)])
    for a in range(int(math.ceil(max_sqrt))):
        if (a + ((n-a*a)**2)) == m:
            result+=1
    return result


def main():
    print solution(18,198)



if __name__ == '__main__':
    main()