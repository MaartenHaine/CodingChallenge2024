'''
string = \
"The whole world spoke one language until ChatGPT came with its multiple languages. " \
"It has turned the world in a riot, because they can't seem to understand each other anymore. " \
"It is your task to gather words from this explanation in a list. " \
"In this list there should be no double words and no punctuation marks. " \
"The words in the list should have the same sequence as given by the string and all words should be lowercase. " \
"When there are double words keep the first in the sequence. " \
"Good luck!"
'''

### INPUT - DO NOT TOUCH
string = eval(input())
### END INPUT

def gatherWords(string: str) -> list:
    word = ""
    for letter in string:
        if letter.isalpha() or letter == " ":
            word += letter
    string = word
    wordSet = []
    wordList = string.split()
    for word in wordList:
        word = word.lower()
        if word not in wordSet:
            wordSet.append(word)
    return wordSet


print(gatherWords(string))
