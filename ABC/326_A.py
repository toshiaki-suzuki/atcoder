X, Y = map(int, input().split())
diff = X - Y
ans = "Yes"
if diff > 0:
    if diff > 3:
        ans = "No"
else:
    if diff < -2:
        ans = "No"
print(ans)
