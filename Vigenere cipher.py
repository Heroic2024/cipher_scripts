#generating the key to match the length of the plain text
def gen_key(pl_text,keyword):
    keyword = list(keyword)
    if len(pl_text) == len(keyword):
        return keyword
    else:
        for i in range(len(pl_text) - len(keyword)):
            keyword.append(keyword[i%len(keyword)])
    return "".join(keyword)

#Function for Encryption of vigenere cipher
def encrypt(pl_text,keyword):
    result = []
    key = gen_key(pl_text,keyword)
    for i in range(len(pl_text)):
        character = pl_text[i]
        if character.isupper():
            result.append(chr(((ord(character) - 65 + ord(key[i]) - 65) % 26 + 65)))
        elif character.islower():
            result.append(chr(((ord(character) - 97 + ord(key[i]) - 97) % 26 + 97)))
        elif(character == " "):
            result.append(" ")
    
    scrpt = "".join(result)
    return scrpt

#Function for Decryption of vigenere cipher
def decrypt(ciph_text,keyword):
    result = []
    key = gen_key(ciph_text,keyword)
    for i in range(len(ciph_text)):
        character = ciph_text[i]
        if character.isupper():
            char1 = (((ord(character) - 65) - (ord(key[i]) - 65)) + 26)
            result.append(chr((char1 % 26 + 65)))
        elif character.islower():
            char2 = (((ord(character) - 97) - (ord(key[i]) - 97)) + 26)
            result.append(chr((char2 % 26 + 97)))
        elif(character == " "):
            result.append(" ")
    
    decryp_scrpt = "".join(result)
    return decryp_scrpt


#input for encryption
pl_text = str(input("Enter the plain text: "))
keyword = str(input("Enter the key: "))
print(encrypt(pl_text,keyword))

#input for decrpytion
cipher = str(input("Enter the cipher text: "))
key = str(input("Enter the key: "))
print(decrypt(cipher,key))