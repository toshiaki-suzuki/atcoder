N = int(input())

branches = []
for i in range(N):
    branches.append(input().split())

mx = 0

for i in range(24):
    count = 0
    for b in branches:
        w = int(b[0])
        x = int(b[1])
        t = i + x
        if t >= 24:
            t -= 24
        if t >= 9 and t < 18:
            count += w
    if count > mx:
        mx = count

print(mx)
