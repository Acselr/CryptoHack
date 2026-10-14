# Euclid's algorithm
# The Greatest Common Divisor (GCD) is the largest number which divides two positive integers (a,b).

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

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

print(gcd_recursive(12, 8)) # 4
print(gcd_recursive(11, 17)) # 1
print(gcd_recursive(66528, 52920)) # 1512