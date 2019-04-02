# 2에서 N까지의 숫자 중에서 소인수의 최댓값이 M이하인 숫자의 갯수를 구하세요.

def getMax(n):
    for i in range(2, n+1):
        while n % i == 0 :
            max = i
            n /= i
    return max 


n, m = [int(i) for i in input().split()]

result = 0
for i in range(2, n+1):
    if getMax(i) <= m:
        print(getMax(i))
        result += 1
print(result)