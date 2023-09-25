N = input()

ans = "Yes"
for i in range(len(N)-1):
    if i < len(N)-1:
        if N[i+1] >= N[i]:
            ans = "No"
            break
print(ans)
