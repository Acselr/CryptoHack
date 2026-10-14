# extended Euclidean algorithm
# an way to find integers u,v such that a⋅u + b⋅v = gcd⁡(a,b)

# compute the inverse of a mod b
def inverse(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers.")
    
    init_b = b

    p_curr, p_prev = 1, 0
    q_curr, q_prev = -1, -1

    # step 0
    count = 0
    if a < b:
        while a <= b:
            b -= a
            count += 1
    else:
        while b <= a:
            a -= b
            count += 1

    q_prev = count

    # step 1
    count = 0
    if a < b:
        while a <= b:
            b -= a
            count += 1
    else:
        while b <= a:
            a -= b
            count += 1

    q_curr = count
    count = 0

    # step N
    while a > 0 and b > 0:
        if a < b:
            while a <= b:
                b -= a
                count += 1
        else:
            while b <= a:
                a -= b
                count += 1

        temp = p_curr
        p_curr = (p_prev - (p_curr * q_prev)) % init_b
        p_prev = temp

        q_prev, q_curr = q_curr, count
        count = 0

    # add the last step
    return (p_prev - (p_curr * q_prev)) % init_b

# resolve the equation a⋅u + b⋅v = 1
def extended_gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Both a and b must be positive integers.")
    
    u = inverse(a, b)
    v = (1-min(a,b)*u)//max(a,b)

    return (u, v)


#print(extended_gcd(15,26)) # 7 , -4
#print(extended_gcd(26513,32321))

#print(extended_gcd(3,13))