# Euclide's algorithm

def gcd(a, b):
    while a > 1 and b > 1:
        if a == b:
            return a
        elif a > b:
            a = a - b
        else:
            b = b - a
    return 1

print(gcd(12, 8)) # 4
print(gcd(11, 17)) # 1
print(gcd(66528, 52920)) # 1512