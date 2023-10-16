S = input()

ans = "Yes"
for i in range(len(S)):
    if i % 2 == 1 and S[i] != "0":
        ans = "No"
        break

print(ans)
