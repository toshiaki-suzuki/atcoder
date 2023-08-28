N = int(input())
P = list(map(int, input().split()))

if N == 1:
  print(0)
  exit()

p1 = P.pop(0)
saikyo = max(P)

if saikyo < p1:
  print(0)
else:
  print(saikyo - p1 + 1)
  