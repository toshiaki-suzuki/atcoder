B = int(input())

ans = -1
A = 1

while A**A <= B:
    if A ** A == B:
        ans = A
        break
    A += 1

print(ans)
