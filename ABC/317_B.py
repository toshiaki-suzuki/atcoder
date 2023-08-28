N = int(input())
A = list(map(int, input().split()))

A.sort()
for i in range(N-1):
    d = A[i+1]-A[i]
    if d == 1:
        continue
    print(A[i]+1)
    break
