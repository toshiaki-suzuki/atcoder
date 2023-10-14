N = int(input())
A = list(map(int, input().split()))

ans = "Yes"
for i in range(N):
    if A[0] != A[i]:
        ans = "No"
        break
print(ans)
