'''
Playful cipher
https://www.youtube.com/watch?v=OuSX8T-uTuQ

I was thinking about getting an encrypted keyword which they need to decrypt with their previous cypher exercise.
'''

def create_playfair_square(phrase):
    key = key.replace('J', 'I').upper() + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = "".join(dict.fromkeys(key)) 
    grid = [[k for k in key[i:i+5]] for i in range(0, 25, 5)]
    return grid

def find_location(grid, char):
    for i in range(0, 5):
        for j in range(0, 5):
            if grid[i][j] == char:
                return i, j


def playfair_encrypt(message: str, key: str) -> str:
    playfair_square = create_playfair_square(key)
    ciphertext = ''

    # Remove non-alphabetic characters
    message = "".join(filter(str.isalpha, message))

    # Handle repeating letters by inserting 'X' between them
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i+1]:
            message = message[:i+1] + 'X' + message[i+1:]
        i += 1
    
    # Append 'X' if the last block only contain a single character
    if len(message) % 2 == 1:
        message += 'X'

    # For each digraphs, substitute the characters using the grid
    for i in range(0, len(message), 2):
        digraph = message[i:i+2]
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            sub1 = playfair_square[row1][(col1 + 1) % 5]
            sub2 = playfair_square[row2][(col2 + 1 ) % 5]
        elif col1 == col2:
            sub1 = playfair_square[(row1 + 1) % 5][col1]
            sub2 = playfair_square[(row2 + 1) % 5][col2]
        else:
            sub1 = playfair_square[row1][col2]
            sub2 = playfair_square[row2][col1]
        
        ciphertext += sub1 + sub2

    return ciphertext


def playfair_decrypt(ciphertext: str, key: str) -> str:
    playfair_square = create_playfair_square(key)
    message = ''

    # For each digraphs, substitute the characters using the grid
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        row1, col1 = find_location(playfair_square, digraph[0])
        row2, col2 = find_location(playfair_square, digraph[1])
        if row1 == row2:
            sub1 = playfair_square[row1][(col1 - 1) % 5]
            sub2 = playfair_square[row2][(col2 - 1 ) % 5]
        elif col1 == col2:
            sub1 = playfair_square[(row1 - 1) % 5][col1]
            sub2 = playfair_square[(row2 - 1) % 5][col2]
        else:
            sub1 = playfair_square[row1][col2]
            sub2 = playfair_square[row2][col1]
        
        message += sub1 + sub2

    # Remove the 'X' between two similar letters
    i = 0
    while i < len(message) - 2:
        if message[i] == message[i+2] and message[i+1] == 'X':
            message = message[:i+1] + message[i+2:]
        i += 1

    # Remove the last 'X'
    if message[-1] == 'X':
        message = message[:-1]

    return message

