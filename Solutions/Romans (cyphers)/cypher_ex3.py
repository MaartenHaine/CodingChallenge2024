"""

https://www.youtube.com/watch?v=OuSX8T-uTuQ

You want to encrypt text so that the enemies can't read it, create the cipher instead of decrypting it this time.

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

    "H" and "E" form a rectangle, so they are replaced with "C" and "G."
"""
### DO NOT
#key = eval(input())
#text = eval(input())
##


# Function to convert the string to lowercase
def to_lowercase(text):
   return text.lower()

# Function to remove all spaces in a string
def remove_spaces(text):
   new_text = ""
   for char in text:
      if char != " ":
         new_text += char
   return new_text

# Function to group 2 elements of a string
def group_characters(text):
   groups = []
   group_start = 0
   for i in range(2, len(text), 2):
      groups.append(text[group_start:i])
      group_start = i
   groups.append(text[group_start:])
   return groups

# Function to fill a letter in a string element
def fill_letter(text):
   k = len(text)
   if k % 2 == 0:
      for i in range(0, k, 2):
         if text[i] == text[i+1]:
            new_word = text[0:i+1] + str('x') + text[i+1:]
            new_word = fill_letter(new_word)
            break
         else:
            new_word = text
   else:
      for i in range(0, k-1, 2):
         if text[i] == text[i+1]:
            new_word = text[0:i+1] + str('x') + text[i+1:]
            new_word = fill_letter(new_word)
            break
         else:
            new_word = text
   return new_word

# Generating the 5x5 key square matrix
def generate_key_matrix(word):
   alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   key_letters = []
   for char in word:
      if char not in key_letters:
         key_letters.append(char)

   complementary_elements = []
   for char in key_letters:
      if char not in complementary_elements:
         complementary_elements.append(char)
   for char in alphabet_list:
      if char not in complementary_elements:
         complementary_elements.append(char)

   matrix = []
   while complementary_elements != []:
      matrix.append(complementary_elements[:5])
      complementary_elements = complementary_elements[5:]

   return matrix

# Searching for an element in the matrix
def search_element(matrix, element):
   for i in range(5):
      for j in range(5):
         if matrix[i][j] == element:
            return i, j

# Encryption using Row Rule
def encrypt_row_rule(matrix, e1_row, e1_column, e2_row, e2_column):
   char1 = ''
   if e1_column == 4:
      char1 = matrix[e1_row][0]
   else:
      char1 = matrix[e1_row][e1_column+1]

   char2 = ''
   if e2_column == 4:
      char2 = matrix[e2_row][0]
   else:
      char2 = matrix[e2_row][e2_column+1]

   return char1, char2

# Encryption using Column Rule
def encrypt_column_rule(matrix, e1_row, e1_column, e2_row, e2_column):
   char1 = ''
   if e1_row == 4:
      char1 = matrix[0][e1_column]
   else:
      char1 = matrix[e1_row+1][e1_column]

   char2 = ''
   if e2_row == 4:
      char2 = matrix[0][e2_column]
   else:
      char2 = matrix[e2_row+1][e2_column]

   return char1, char2

# Encryption using Rectangle Rule
def encrypt_rectangle_rule(matrix, e1_row, e1_column, e2_row, e2_column):
   char1 = matrix[e1_row][e2_column]
   char2 = matrix[e2_row][e1_column]

   return char1, char2

# Encrypting text using the Playfair Cipher
def encrypt_playfair_cipher(matrix, plaintext_list):
   cipher_text = []
   for i in range(0, len(plaintext_list)):
      char1 = 0
      char2 = 0
      ele1_x, ele1_y = search_element(matrix, plaintext_list[i][0])
      ele2_x, ele2_y = search_element(matrix, plaintext_list[i][1])

      if ele1_x == ele2_x:
         char1, char2 = encrypt_row_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
      elif ele1_y == ele2_y:
         char1, char2 = encrypt_column_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)
      else:
         char1, char2 = encrypt_rectangle_rule(matrix, ele1_x, ele1_y, ele2_x, ele2_y)

      cipher = char1 + char2
      cipher_text.append(cipher)
   return cipher_text

def encrypt(text, key):
    text_plain = remove_spaces(to_lowercase(text))
    plaintext_list = group_characters(fill_letter(text_plain))
    if len(plaintext_list[-1]) != 2:
        plaintext_list[-1] = plaintext_list[-1] + 'z'

    #print("The Key text:", key)
    key = to_lowercase(key)
    matrix = generate_key_matrix(key)

    #print("The Plain Text:", text_plain)
    cipher_list = encrypt_playfair_cipher(matrix, plaintext_list)

    cipher_text = ""
    for i in cipher_list:
        cipher_text += i
    #print("The CipherText:", cipher_text)
    return cipher_text

# Test Cases
print(encrypt("I want this message to be encoded", "key"))
print(encrypt("With this plan we can stop chatgpt from ruining this timeline", "antichatgptkeyI"))
print(encrypt("At last we will win", "superdupersecretbestestkey"))

##OUTPUT##
#print(encrypt(text, key))
