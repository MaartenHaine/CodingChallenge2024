"""
It appears that you had a mole on your side.
You want to encrypt text so that the enemies can't read it, create the cipher instead of decrypting it this time.
This time with a cipher ChatGPT will have difficulty against!

The Playfair cipher.
https://www.youtube.com/watch?v=OuSX8T-uTuQ

Create a 5x5 Grid Key Square:
    First, create a 5x5 grid using a keyword, omitting duplicate letters and typically combining I and J into a single cell (since there are only 25 squares for the 26 letters).
    The remaining letters of the alphabet are then filled in the grid.

Encrypting the Message:
    Break the plaintext message into pairs of letters (digraphs). 
    If a pair has two of the same letters, like "LL," insert a filler (usually "X") between them, turning it into "LX."
    If the pair falls in the same row of the grid, each letter is replaced with the one 
    immediately to its right (wrapping around to the start of the row if necessary).
    If the pair falls in the same column, each letter is replaced by the one directly below it (wrapping to the top if necessary).
    If the pair forms a rectangle, each letter is replaced by the one in its row but in the other letter's column.

Example

With a keyword "MONARCHY," the grid might look like this:

mathematica

M O N A R
C H Y B D
E F G I/J K
L P Q S T
U V W X Z

For the digraph "HE":

    "H" and "E" form a rectangle, so they are replaced with "C" and "F".
"""
### DO NOT
key = eval(input())
text = eval(input())
##


def encrypt(ciphertext: str, key: str) -> str:
    #TODO
    return ""

##OUTPUT##
print(encrypt(text, key))

# Example tests
assert(encrypt("I want this message to be encoded", "key") == "mugsszzonplyxaxgdaztkyalhildgv")
assert(encrypt("With this plan we can stop chatgpt from ruining this timeline", "antichatgptkeyI") == "xtapapcredntzpanconqetyhnpdprxqomxctctpnkaqcarlsctkz")
assert(encrypt("At last we will win", "superdupersecretbestestkey") == "fcvlpdxpqmnvmvlo")