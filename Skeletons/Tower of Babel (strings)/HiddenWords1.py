"""
There are words hidden in plain sight, namely inside already gathered words.
These words can be found by only selecting a few letters of word sequences.
Given is an extra list of words, check which words can already be found by using the gathered words.

In this excercise you should only look at adjacent words in a sentence and respect the order in which they are said.
For example, take "this" + "exercise" -> "he", but "exercise" + "this" -x-> "he".

Example:
    sentence_words = ["This", "exercise", "is", "pretty", "interesting"]
    possible_words = ["ex", "resting", "see", "text", "set"]
    Hiddenwords should return ["ex", "resting, "see", "set"] because of:
    EXercise        -> EX
    inteRESTING     -> RESTING
    thiS + ExErcise -> SEE
    This + EXErcisE -/> TEXT
    iS + prETTy     -> SETT -> SET
"""


### INPUT - DO NOT TOUCH
sentence_words = eval(input())
possible_words = eval(input())
### END INPUT


def hiddenWords(lijst: list[str], possibleWords: list[str]) -> list:
    return []


print(hiddenWords(sentence_words, possible_words))
