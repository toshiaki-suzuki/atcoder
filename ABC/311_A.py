N = int(input())
S = input()

alf = []
for i in range(N):
    alf.append(S[i])
    if "A" in alf and "B" in alf and "C" in alf:
        print(i + 1)
        break
