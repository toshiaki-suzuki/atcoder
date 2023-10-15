def calc(s, t):
    # tの文字数までループを回します。
    for i in range(len(t)):
        # sの文字数を超えた場合は、sの文字数を返します。
        if i >= len(s):
            return len(s)
        # sとtの文字が一致しない場所が見つかった場合、その位置を返します。
        if s[i] != t[i]:
            return i
    # tのすべての文字がsと一致した場合は、tの文字数を返します。
    return len(t)


# nとt2を入力として受け取ります。
n, t2 = input().split()
n = int(n)  # nを整数に変換します。

# 各配列の初期化を行います。
s = [''] * (n + 1)  # サイズ (n+1) のリストで初期化。0番目の要素は使用しないため。
a = [0] * (n + 1)
b = [0] * (n + 1)

# sの各要素を入力として受け取ります。
for i in range(1, n + 1):
    s[i] = input()

# sの各要素とt2との比較を行い、一致する文字数をaに格納します。
for i in range(1, n + 1):
    a[i] = calc(s[i], t2)

# t2を反転します。
t2 = t2[::-1]
# sの各要素を反転し、t2との比較を行い、一致する文字数をbに格納します。
for i in range(1, n + 1):
    s[i] = s[i][::-1]
    b[i] = calc(s[i], t2)

ans = []
# sの各要素について、特定の条件を満たすかチェックし、満たす場合は答えとしてansに追加します。
for i in range(1, n + 1):
    t = s[i]
    flag = False
    # 以下の条件を確認します。
    if a[i] == len(t) and len(t) == len(t2):
        flag = True
    if a[i] + b[i] >= len(t) and len(t) + 1 == len(t2):
        flag = True
    if a[i] + b[i] >= len(t) - 1 and len(t) - 1 == len(t2):
        flag = True
    if a[i] + b[i] == len(t) - 1 and len(t) == len(t2):
        flag = True
    if flag:
        ans.append(i)

# 答えとなる要素数と、それらの要素を出力します。
print(len(ans))
for x in ans:
    print(x, end=' ')
print()
