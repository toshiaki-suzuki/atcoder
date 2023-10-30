N, M = map(int, input().split())
G = [input() for _ in range(N)]


def check9(x, y):
    if x > M - 9 or y > N - 9:
        return False

    # 左上の3x3の黒色チェック
    for i in range(3):
        for j in range(3):
            if G[y + i][x + j] != "#":
                return False

    # 右下の3x3の黒色チェック
    for i in range(6, 9):
        for j in range(6, 9):
            if G[y + i][x + j] != "#":
                return False

    # 14マスの白色チェック
    for i in range(3):
        if G[y + i][x + 3] != "." or G[y + 3][x + i] != ".":
            return False
    for i in range(6, 9):
        if G[y + i][x + 5] != "." or G[y + 5][x + i] != ".":
            return False

    return True


for i in range(N - 8):
    for j in range(M - 8):
        if check9(j, i):
            print(i + 1, j + 1)
