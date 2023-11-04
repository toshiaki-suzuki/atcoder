N = int(input())
S = input()

ans = "No"
for i in range(N - 1):
    s = S[i] + S[i + 1]
    if s == "ab" or s == "ba":
        ans = "Yes"
        break
print(ans)
