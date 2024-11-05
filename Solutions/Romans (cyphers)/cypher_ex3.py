'''
Playful cipher
https://www.youtube.com/watch?v=OuSX8T-uTuQ

I was thinking about getting an encrypted keyword which they need to decrypt with their previous cypher exercise.
'''
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

def cipher_encrypt(text, key):
    text_plain = remove_spaces(to_lowercase(text))
    plaintext_list = group_characters(fill_letter(text_plain))
    if len(plaintext_list[-1]) != 2:
        plaintext_list[-1] = plaintext_list[-1] + 'z'

    print("The Key text:", key)
    key = to_lowercase(key)
    matrix = generate_key_matrix(key)

    print("The Plain Text:", text_plain)
    cipher_list = encrypt_playfair_cipher(matrix, plaintext_list)

    cipher_text = ""
    for i in cipher_list:
        cipher_text += i
    print("The CipherText:", cipher_text)
    return cipher_text

# Test Cases
print(cipher_encrypt("hello", "key"))
print(cipher_encrypt("hello", "longkey"))
print(cipher_encrypt("Idontliketestcases", "longkeylongkey"))


