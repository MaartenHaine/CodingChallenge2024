"Vigenere encryption"

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
