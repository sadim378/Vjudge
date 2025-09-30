n = input()

n = n.replace('1', 'x')  # 1 -> x (temporary)
n = n.replace('9', '1')  # 9 -> 1
n = n.replace('x', '9')  # x -> 9

print(n)
