def solve (N, workload):
    big = 0
    temp = 0
    for i in range(N-1):
        if workload[i] > 6:
            temp += 1
        else:
            if temp > big:
                big = temp
            temp = 0
    return big

N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print (out_)
