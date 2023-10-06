N, M = map(int, input().split())
A = list(map(int, input().split()))

a_count = 0
for i in range(1, N + 1):
    if i == A[a_count]:
        print(0)
        a_count += 1
    else:
        print(A[a_count] - i)
