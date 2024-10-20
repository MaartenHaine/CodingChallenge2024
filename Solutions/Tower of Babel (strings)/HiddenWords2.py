"""
There are words hidden in plain sight, namely inside already gathered words.
These words can be found by only selecting a few letters of word sequences.
Given is an extra list of words, check which words can already be found by using the gathered words.

The words can be found by putting multiple words together and filtering their letters.
Take for example the sequence:
 "This exercise is pretty interesting"
In the sentence, words like, "ex", "resting" and even "he" can be found.
We can find the word "he" by taking "this" and "exercise", this gives "thisexercise" as a result.
If we now filter the string to only use "h" and "e", we get "heee", wherein "he" can be found.
Pretty simple right?
For a more complicated example, take:
 "There was once a little octopus"
A needed note is that we can add as many words together as we need.
These words don't have to be next to eachother, but they have to follow the same sequence as the sentence.
In this example we can use "there" + "was" + "octopus" to get "react", but we can't get "ui" from "octopus" + "little".
Good Luck
"""


#sentence_words = ["This", "exercise", "is", "pretty", "interesting"]
#possible_words = ["ex", "resting", "thing", "init", "dol", "he", "turn", "toch", "body", "under", "an"]

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


def extend(cutlijst, index, part_sol):
    lijst = []
    for i in range(index+1, len(cutlijst)):
        lijst.append([i, part_sol+cutlijst[i]])
    return lijst


def recursiveSearch(pword : str, cutlijst: list[str], index = -1, part_sol = None):
    if part_sol is None:
        copylijst = cutlijst
        cutlijst = []
        letters = gatherLetters(pword)
        for cword in copylijst:
            newword = keepLetters(cword, letters)
            if len(newword) > 0:
                cutlijst.append(newword)
        if len(cutlijst) == 0:
            return False
        part_sol = ""

    if pword in part_sol: #look if we found a solution
        return True

    for i in range(len(pword)): #examine if the solution is still possible
        if part_sol.endswith(pword[:i+1]) or part_sol == "":
            break
    else:
        return False

    for item in extend(cutlijst, index, part_sol): #extend part_sol
        #print(item)
        if recursiveSearch(pword, cutlijst, item[0], item[1]): #try again with new part_sols
            return True
    return False


def hiddenWords(lijst: list[str], possibleWords: list[str]) -> list:
    pwords = []
    for pword in possibleWords: #iterate the given possible words
        cutlijst = []
        letters = gatherLetters(pword)
        for word in lijst: #iterate over lijst and remove all unnecessairy letters
            word = keepLetters(word, letters)
            if len(word.rpartition(pword)[0]) != 0 or len(word.rpartition(pword)[1]) != 0: #check if word is already found
                pwords.append(pword)
                break
            if len(word) > 0:
                cutlijst.append(word) #append non empty words
        else:
            if recursiveSearch(pword, cutlijst): #check if a possible summation of words is possible
                pwords.append(pword)
    return pwords

print(hiddenWords(sentence_words, possible_words))

