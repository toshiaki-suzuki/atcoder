N = int(input())
A = list(map(int, input().split()))

mx = max(A)
A.remove(mx)
newA = [a for a in A if a != mx]
ans = max(newA)

print(ans)
