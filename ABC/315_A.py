S = input()

ans = [s for s in S if not (s in ["a", "e", "i", "o", "u"])]
print("".join(ans))
