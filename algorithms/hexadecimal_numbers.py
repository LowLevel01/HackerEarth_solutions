from math import gcd

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    n = 0
    
    for x in range(l, r+1):
        a = x
        s = 0
        while a != 0:
            s += a % 16
            a = a//16
        if gcd(x, s) > 1:
            n += 1
    print(n)
