t = int(input())
for _ in range(t):
    n=int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = A[0] ^ A[1]
    for i in range(1, n-1):
        exp = A[i] ^ A[i+1]
        if exp < m:
            m = exp
    print(m)
    
#explanation: (x and y) xor (x or y) can be simplified into x^y
# looking at the truth table of the xor operation we find out that two numbers that have similar binary representations when xor'ed give a small number
# That's the reason we sort, to look at pairs which have a similar binary representations.
