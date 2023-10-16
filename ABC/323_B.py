N = int(input())
S = [input() for _ in range(N)]

nums = {}
for i in range(N):
    cnt = 0
    for s in S[i]:
        if s == "o":
            cnt += 1
    nums[i + 1] = cnt

ans = []
# xには辞書の(key,value)のタプルが入る
# x[1]には辞書の値が入る
# つまり、-x[1]により、valueの降順にソートしている
for k, v in sorted(nums.items(), key=lambda x: -x[1]):
    ans.append(k)

print(*ans)
