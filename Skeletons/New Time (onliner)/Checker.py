"""
validate the onliner by counting the amount of lines in the program.
and checking a few test cases
"""
from Challenge import *
LINES_OF_CODE = 17

def test_challenge() -> bool:
    # ------- validate number of lines -------
    # todo: only read lines in the function, make it runnable from diff directories
    with open("Challenge.py") as f:
        lines = len(f.readlines()) 

    if LINES_OF_CODE != lines:
        print(f"Incorrect number of lines ({LINES_OF_CODE - lines})")
        return False
    
    # ------- validate test cases -------
    # Check message length constraint
    long_message = "A" * 257
    if validate(long_message):
        print("allows long messages")
        return False
    
    short_message = "A" * 256
    if not validate(short_message):
        print("does not allow short messages")
        return False

    # Check if illegal characters are allowed
    message = "'"
    if validate(message):
        print("allows invalid characters")
        return False
    
    # check if long numerical sequences are allowed
    if validate("1234567891011"):
        print("allows long numerical sequences")
        return False
    
    # check if splitted long numerical sequences are allowed
    if validate("123456 + 7891011"):
        print("allows long numerical sequences")
        return False
    return True


print(test_challenge())
