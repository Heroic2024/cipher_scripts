def checkPrime(key_a):
    if 1 < key_a <= 26:
        for i in range(2, (key_a // 2) + 1):
            if key_a % i == 0:
                return False
        return True
    else:
        print("Not valid")
        return False

def encrypt(pl_text, key_a, key_b):
    if not checkPrime(key_a):
        print("Error: key_a is not prime")
        return ""
    
    result = []
    for char in pl_text:
        if char.isupper():
            x = ord(char) - 65
            result.append(chr(((key_a * x + key_b) % 26) + 65))
        elif char.islower():
            x = ord(char) - 97
            result.append(chr(((key_a * x + key_b) % 26) + 97))
        elif char == " ":
            result.append(" ")
    return "".join(result)

def decrypt(ciph_txt, a, b):
    a_inv = -1
    for i in range(1, 27):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    
    if a_inv == -1:
        print("Error: Modular inverse of a does not exist")
        return ""
    
    result = []
    for char in ciph_txt:
        if char.isupper():
            res = ord(char) - 65
            result.append(chr((a_inv * (res - b + 26) % 26) + 65))
        elif char.islower():
            res = ord(char) - 97
            result.append(chr((a_inv * (res - b + 26) % 26) + 97))
        elif char == " ":
            result.append(" ")
    return "".join(result)

# Main program
pl_text = input("Enter the plain text: ")
key_a = int(input("Enter the prime key: "))
key_b = int(input("Enter the second key: "))
encrypted = encrypt(pl_text, key_a, key_b)
print("Encrypted text:", encrypted)

ciph = input("Enter the cipher text: ")
a = int(input("Enter the prime key: "))
b = int(input("Enter the second key: "))
decrypted = decrypt(ciph, a, b)
print("Decrypted text:", decrypted)
