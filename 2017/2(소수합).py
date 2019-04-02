# N <= X <= M 인 모든 소수 X의 합을 구하세요.

# 에라토스테네스의 체
def primeNumberSieve(start, size):
    a = []
    _sum = 0
    for i in range(size+1):
        a.append(i)
    for i in range(2, size+1):
        if a[i] == 0:
            continue
        j = i*2
        while j <= size:
            a[j] = 0
            j += i
    for i in range(start, size+1):
        if a[i] != 0:
            _sum += 1
    if _sum != 0:
        print(_sum)
    else:
        print(-1)
               

n, m = [int(i) for i in input().split()]
primeNumberSieve(n,m)