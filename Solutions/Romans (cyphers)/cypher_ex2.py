"""
Vigenere cipher

input: encrypted text, key
output: decrypted text

the given key is encrypted and you have to use your previous caesar cipher to decrypt it.
The shift they used to encrypt this key is the length of the encrypted text.
"""

### DO NOT
key = eval(input())
text = eval(input())
##

def caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isupper():
            decrypted_char = chr(((ord(char) - 65 - shift) % 26) + 65)
        elif char.islower():
            decrypted_char = chr(((ord(char) - 97 - shift) % 26) + 97)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_repeated = key * (len(plain_text) // len(key)) + key[:len(plain_text) % len(key)]
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if plain_text[i].isupper():
                encrypted_char = chr((ord(plain_text[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_char = chr((ord(plain_text[i]) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += plain_text[i]
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_repeated = key * (len(encrypted_text) // len(key)) + key[:len(encrypted_text) % len(key)]
    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord('A')
            if encrypted_text[i].isupper():
                decrypted_char = chr((ord(encrypted_text[i]) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_char = chr((ord(encrypted_text[i]) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += encrypted_text[i]
    return decrypted_text

def cipher_decrypt(text, key):
    decrypted_key = caesar_cipher(key, -len(text))
    #print(decrypted_key)
    return vigenere_decrypt(text, decrypted_key)

def cipher_encrypt(text, key):
    encrypted_key = caesar_cipher(key, len(text))
    #print(encrypted_key)
    return vigenere_encrypt(text, key)

#print(cipher_encrypt("hello", "key"))
#print(cipher_decrypt("rijvs", "fzt"))
#print("#########")
#print(cipher_encrypt("hello", "longkey"))
#print(cipher_decrypt("ssyry", "gjibfzt"))
#print("#########")
#print(cipher_encrypt("I am very cool", "longkeylongkey"))
#print(cipher_decrypt("T ns zccm iysj", "xazswqkxazswqk"))
#print("#########")

##OUTPUT##
print(cipher_decrypt(text, key))
