"""
There are words hidden in plain sight, namely inside already gathered words.
These words can be found by only selecting a few letters of word sequences.
Given is an extra list of words, check which words can already be found by using the gathered words.
"""

dictionairy = ["This", "excercise", "is", "pretty", "interesting"]
extra_words = ["ex", "resting", "thing", "init", "dol", "he", "turn", "toch", "body", "under", "an"]

longer = ['The', 'world', 'of', 'language', 'has', 'been', 'turned', 'to', 'chaos', 'nobody', 'can', 'understand', 'another', 'It', 'is', 'your', 'task', 'gather', 'words', 'from', 'this', 'explanation', 'In', 'a', 'list', 'there', 'should', 'be', 'no', 'double', 'and', 'punctuation', 'marks', 'Good', 'luck']

def gatherLetters(word: str):
    letters = set()
    for letter in word.lower():
        letters.add(letter)
    return letters


def hiddenWords(lijst: list[str], possibleWords: list[str]):
    pwords = []
    for pword in possibleWords:
        cutlijst = []
        letters = gatherLetters(pword)
        for word in lijst:
            word = word.lower()
            for letter in word:
                if letter not in letters:
                    word = word.replace(letter, '')
                    #print(letters, word)
            if len(word.rpartition(pword)[0]) != 0 or len(word.rpartition(pword)[1]) != 0:
                pwords.append(pword)
                break
            if len(word) > 0:
                cutlijst.append(word)
        else:
            #print(cutlijst)
            totalword = ""
            for cword in cutlijst:
                totalword += cword
            #print(totalword)
            if len(totalword.rpartition(pword)[0]) != 0 or len(totalword.rpartition(pword)[1]) != 0:
                pwords.append(pword)
    return pwords

print(hiddenWords(dictionairy, extra_words))
print(hiddenWords(longer, extra_words))
