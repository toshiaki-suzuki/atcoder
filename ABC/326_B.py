N = input()
ans = int(N)

while True:
    n = str(ans)
    thr = int(n[0])
    sec = int(n[1])
    fir = int(n[2])
    if thr * sec == fir:
        break
    ans += 1
print(ans)
