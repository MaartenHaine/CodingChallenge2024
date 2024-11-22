"""
There are words hidden in plain sight, namely inside already gathered words.
These words can be found by only selecting a few letters of word sequences.
Given is an extra list of words, check which words can already be found by using the gathered words.

In this excercise you should only look at adjacent words in a sentence and respect the order in which they are said.
For example, take "tHis" + "ExErcisE" -> "he", but "ExErcisE" + "tHis" -x-> "he".
"""


#sentence_words = ['There', 'was', 'once', 'a', 'little', 'octopus']
#possible_words = ["ex", "resting", "thing", "init", "dol", "he", "turn", "toch", "body", "under", "an", "react", "stop"]

### INPUT - DO NOT TOUCH
sentence_words = eval(input())
possible_words = eval(input())
### END INPUT


def gatherLetters(word: str): #puts the letters of a word in a set
    letters = set()
    for letter in word.lower():
        letters.add(letter)
    return letters


def keepLetters(word, letters): #replaces all other characters than given by letters from word
    word = word.lower()
    for letter in word:
        if letter not in letters:
            word = word.replace(letter, '')
            # print(letters, word)
    return word


def hiddenWords(lijst: list[str], possibleWords: list[str]) -> list:
    pwords = []
    for pword in possibleWords: #iterate the given possible words
        longword = ""
        letters = gatherLetters(pword)
        for word in lijst: #iterate over lijst and remove all unnecessairy letters
            word = keepLetters(word, letters)
            if len(word.rpartition(pword)[0]) != 0 or len(word.rpartition(pword)[1]) != 0: #check if word is already found
                pwords.append(pword)
                break
            if len(word) > 0:
                longword += word
        else:
            if len(longword) > 0:
                if len(longword.rpartition(pword)[0]) != 0 or len(longword.rpartition(pword)[1]) != 0: #check if word is already found
                    pwords.append(pword)
    return pwords

print(hiddenWords(sentence_words, possible_words))