"""
Chatgpt has given Ceasar's cypher to the enemies before ceasar has made it himself. Give Ceasar the algoritm to break it before it changes hisotry too much.
The shift will be given.

input: encrypted text
output: decrypted text
"""

### DO NOT TOUCH ###

text = eval(input())
shift = eval(input())

### END ###

def cipher_decrypt(text, shift):
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


#print(caesar_cipher("mxpvewsxritmqszwezspewvzCICRQIMSDQTEPLERPTPSRLJPE", 12))

#print(caesar_cipher("longkey", 5))

##OUTPUT##
print(cipher_decrypt(text, shift))