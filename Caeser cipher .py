#function for decrypption
def encrypt(pl_text,key):
    result = []
    for i in range(len(pl_text)):
        character = pl_text[i]

        if(character.isupper()):
            result += chr((ord(character) - 65 + key) % 26 + 65)
        elif(character.islower()):
            result += chr((ord(character) - 97 + key) % 26 + 97)
        elif(character == " "):
            result += " "
    
    scrpt = "".join(result)
    return scrpt

#function for decryption
def decrypt(cipher_txt,key):
    result = []
    for i in range(len(cipher_txt)):
        character = cipher_txt[i]

        if(character.isupper()):
            result += chr((ord(character) - 65 - key) % 26 + 65)
        elif(character.islower()):
            result += chr((ord(character) - 97 - key) % 26 + 97)
        elif(character == " "):
            result += " "
    
    decryp_scrpt = "".join(result)
    return decryp_scrpt

#function for brute force attack
def brute_force(cpr_txt):
    results = []
    for i in range (25):
        result = []
        for j in range(len(cpr_txt)):
            character = cpr_txt[j]

            if(character.isupper()):
                result += chr((ord(character) - 65 - i) % 26 + 65)
            elif(character.islower()):
                result += chr((ord(character) - 97 - i) % 26 + 97)
            elif(character == " "):
                result += " "
            
        decryp_scrpt = "".join(result)
        results.append((decryp_scrpt,i))
    
    for decryp_scrpt, i in results:
        print(f"Key {i}: {decryp_scrpt}")


#Enter the key and plain text for decrypption
pl_text = str(input("Enter the plain text: "))
key = int(input("Enter the key: "))
print(encrypt(pl_text,key))

#Enter the key and cipher text for decryption
cipher_txt = str(input("Enter the cipher text: "))
cipher_key = int(input("Enter the cipher key: "))
print(decrypt(cipher_txt,cipher_key))

#Enter the cipher text for brute force attack
cpr_txt = str(input("Enter the cipher text: "))
brute_force(cpr_txt)