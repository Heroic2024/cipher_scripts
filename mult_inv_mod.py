def mult_inv(a):
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i
    return -1

print(mult_inv(7))