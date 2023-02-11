t  = int(input())
for _ in range(testCase):
    n, k = map(int,input().split())
    l = list(map(int,input().split()))
    m = k % n          #if k > n then a rotation by k is equivalent to a rotation by k%n
    print(*(l[n-m:]+l[:n-m]))        # a rotation by m is equivalent to dividing the list l into two lists l[n-m:] and l[:n-m] and exchanging them

    
#note: putting * before a list passes every single elements through print
#example: print(*[1,2,3]) would give: 1 2 3
