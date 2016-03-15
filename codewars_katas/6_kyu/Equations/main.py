import math
def solution(n, m):
    result = 0
    for a in range(int(math.ceil(max([math.sqrt(n), math.sqrt(m)]))+1)):
        if (a + (n-a**2)**2) == m and (a**2 + int(math.sqrt(m-a)) == n):
                result+=1
    return result
def main():
    print solution(4, 20)



if __name__ == '__main__':
    main()