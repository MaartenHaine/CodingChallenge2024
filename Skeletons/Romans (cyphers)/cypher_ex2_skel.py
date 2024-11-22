"""
The cunning group managed to get a more complicated encryption from ChatGPT.
This one is called the Vigenere cipher.

input: encrypted text, key
output: decrypted text

the given key is encrypted and you have to use your previous caesar cipher to decrypt it. 
The shift they used to encrypt this key is the length of the encrypted text.
"""

### DO NOT
key = eval(input())
text = eval(input())
##


def cipher_decrypt(text: str, key: str) -> str:
    #TODO
    return ""

##OUTPUT##
print(cipher_decrypt(text, key))