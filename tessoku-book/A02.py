N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = "No"
for a in A:
    if a == X:
        ans = "Yes"
        break
print(ans)
