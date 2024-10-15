"""
There are words hidden in plain sight, namely inside already gathered words.
These words can be found by only selecting a few letters of word sequences.
Given is an extra list of words, check which words can already be found by using the gathered words.

In this excercise you should only look at adjacent words in a sentence and respect the order in which they are said.
For example, take "this" + "exercise" -> "he", but "exercise" + "this" -x-> "he".
"""
dictionairy = ["This", "exercise", "is", "pretty", "interesting"]
extra_words = ["ex", "resting", "thing", "init", "dol", "he", "turn", "toch", "body", "under", "an"]

longer = ['The', 'world', 'of', 'language', 'has', 'been', 'turned', 'to', 'chaos', 'nobody', 'can', 'understand', 'another', 'It', 'is', 'your', 'task', 'gather', 'words', 'from', 'this', 'explanation', 'In', 'a', 'list', 'there', 'should', 'be', 'no', 'double', 'and', 'punctuation', 'marks', 'Good', 'luck']

more_long = ['There', 'was', 'once', 'a', 'little', 'octopus']
react = ["react"]


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


def hiddenWords(lijst: list[str], possibleWords: list[str]):
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
        if len(longword) > 0:
            if len(longword.rpartition(pword)[0]) != 0 or len(longword.rpartition(pword)[1]) != 0: #check if word is already found
                pwords.append(pword)
    return pwords

print(hiddenWords(dictionairy, extra_words))
print(hiddenWords(longer, extra_words))
print(hiddenWords(more_long, react + extra_words))