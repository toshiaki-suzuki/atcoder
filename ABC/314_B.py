n = int(input())
c = [0] * (n+1)  # c配列を初期化します。添字が1から始まることを考慮して、サイズを(n+1)にしています。
a = [[] for _ in range(n+1)]  # a配列を2次元リストとして初期化します。

for i in range(1, n+1):
    c[i] = int(input())  # c[i]に整数を読み取ります。
    a[i] = list(map(int, input().split()))  # a[i]の各要素を読み取ります。

x = int(input())  # xを読み取ります。

vec = []
# xと同じ数字がa[i][j]にある場合、iをvecに追加します。
for i in range(1, n+1):
    for j in range(c[i]):
        if a[i][j] == x:
            vec.append(i)

cmin = 37
# vec内の各iに対して、c[i]の最小値を探します。
for i in vec:
    cmin = min(cmin, c[i])

ans = []
# c[i]がcminと同じであるすべてのiをansに追加します。
for i in vec:
    if c[i] == cmin:
        ans.append(i)

print(len(ans))  # ansのサイズを出力します。
print(" ".join(map(str, ans)))  # ansの各要素を出力します。
