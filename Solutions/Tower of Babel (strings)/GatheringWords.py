string = \
"The world of language has been turned to chaos, nobody can understand another. " \
"It is your task to gather words from this explanation in a list. " \
"In this list there should be no double words and no punctuation marks. " \
"Good luck!"


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
