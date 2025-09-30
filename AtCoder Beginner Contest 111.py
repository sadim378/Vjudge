# N = int(input().strip());

# for d in range(1 , 10):
#     val = 111 * d;
# if val >= N:
#     print(val)
    

N = int(input().strip())

for d in range(1, 10):
    val = 111 * d
    if val >= N:
        print(val)
        break
