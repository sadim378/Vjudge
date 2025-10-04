T = int(input())

for _ in range(T):
  nA, nB, nC = map(int, input().split())
  
  result = min(nC, nA + nB)
  print(result)