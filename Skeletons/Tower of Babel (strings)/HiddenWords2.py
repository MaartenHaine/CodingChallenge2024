"""
There are even more words hidden inside already gathered words.
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
These words don't have to be next to each other, but they have to follow the same sequence as the sentence.
In this example we can use "there" + "was" + "octopus" to get "react", but we can't get "ui" from "octopus" + "little".
Good Luck

Example:
    sentence_words = ["There", "was", "once", "a", "little", "octopus"]
    possible_words = ["react", "ui"]
    HiddenWords should return ["react"] because:
    ThERE + wAs + onCE + A + liTTlE + oCTopus
    -> TERE + A + CE + A + TTE + CT
    -> TERE + A + CT                    (skip some words)
    -> TEREACT -> REACT
"""


### INPUT - DO NOT TOUCH
sentence_words = eval(input())
possible_words = eval(input())
### END INPUT


def hiddenWords(lijst: list[str], possibleWords: list[str]) -> list:
    return []


print(hiddenWords(sentence_words, possible_words))
