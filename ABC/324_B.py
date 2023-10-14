N = int(input())

ans = "No"
tmp = N
while tmp % 2 == 0:
    if tmp % 2 == 0:
        tmp = tmp // 2

while tmp % 3 == 0:
    if tmp % 3 == 0:
        tmp = tmp // 3

if tmp == 1:
    ans = "Yes"

print(ans)
