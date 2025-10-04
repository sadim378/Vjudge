from itertools import product

def solve():
    N, K, X = map(int, input().split())
    strings = [input().strip() for _ in range(N)]

    results = []
    for seq in product(strings, repeat=K):
        combined = "".join(seq)   
        results.append(combined)  

    results.sort()  
    print(results[X-1])  
