A = []


def check9(r, c):
    a = []
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            a.append(A[i][j])
    if set(a) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return "Yes"
    else:
        return "No"


for i in range(9):
    A.append(list(map(int, input().split())))

ans = "Yes"
for i in range(9):
    if set(A[i]) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        ans = "No"

if ans != "No":
    for i in range(9):
        col = []
        for j in range(9):
            col.append(A[j][i])
        if set(col) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            ans = "No"
            break

if ans != "No":
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            ans = check9(i, j)
            if ans == "No":
                break
        if ans == "No":
            break
print(ans)
