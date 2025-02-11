import numpy as np

# Input
pl_text = input("Enter plaintext (even length, uppercase letters only): ")
key = list(map(int, input("Enter key matrix (4 space-separated integers): ").split()))



# Convert key matrix to 2x2 format
K = [[key[0], key[1]], [key[2], key[3]]]

# Encryption
c = ""
for i in range(0, len(pl_text), 2):
    pl_matrix = [ord(pl_text[i]) - 65, ord(pl_text[i + 1]) - 65]  # Convert to 0-25
    cipher_matrix = [
        (K[0][0] * pl_matrix[0] + K[0][1] * pl_matrix[1]),
        (K[1][0] * pl_matrix[0] + K[1][1] * pl_matrix[1])
    ]
    cipher_matrix = [x % 26 for x in cipher_matrix]  # Mod 26
    c += chr(cipher_matrix[0] + 65) + chr(cipher_matrix[1] + 65)  # Convert back to letters

print("Ciphertext:", c)

# Decryption
det = K[0][0] * K[1][1] - K[0][1] * K[1][0]  # Determinant
adj = [[K[1][1], -K[0][1]], [-K[1][0], K[0][0]]]  # Adjoint

# Convert negative values in adj to positive
for i in range(2):
    for j in range(2):
        if adj[i][j] < 0:
            adj[i][j] = (adj[i][j] + 26) % 26

# Inverse determinant modulo 26
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

inv_det = mod_inverse(det, 26)

# Calculate inverse key matrix
K_inv = [[(inv_det * adj[i][j]) % 26 for j in range(2)] for i in range(2)]

p = ""
for i in range(0, len(c), 2):
    cipher_matrix = [ord(c[i]) - 65, ord(c[i + 1]) - 65]  # Convert to 0-25
    pl_matrix = [
        (K_inv[0][0] * cipher_matrix[0] + K_inv[0][1] * cipher_matrix[1]),
        (K_inv[1][0] * cipher_matrix[0] + K_inv[1][1] * cipher_matrix[1])
    ]
    pl_matrix = [x % 26 for x in pl_matrix]  # Mod 26
    p += chr(pl_matrix[0] + 65) + chr(pl_matrix[1] + 65)  # Convert back to letters

print("Decrypted Plaintext:", p)    