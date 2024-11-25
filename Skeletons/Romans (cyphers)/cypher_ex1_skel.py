"""
You follow the trail of anomalies back to ancient Rome.
ChatGPT has provided a cypher to some cunning people who want to overthrow Caesar's rule.
This cypher is the famous Caesar cypher, although Caesar hasn't created it yet.
Make an algorithm to decipher the code before they change history!
The shift will be given.

input: encrypted text
output: decrypted text
"""

### DO NOT TOUCH ###

text = eval(input())
shift = eval(input())

### END ###

def cipher_decrypt(text: str, shift: str) -> str:
    #TODO
    return ""

##OUTPUT##
print(cipher_decrypt(text, shift))

### Example tests
assert(cipher_decrypt("Gzcorngpwodgtqpg", 2) == "Examplenumberone")
assert(cipher_decrypt("Cvyknjclskzcpmlc", -2) == "Examplenumberone")
assert(cipher_decrypt("Rovz wo S kw rovn rycdkqo li dro oxowi", 10) == "Help me I am held hostage by the enemy")
assert(cipher_decrypt("100 gyh bupy chpuxyx nby mionbylh auny", 20) == "100 men have invaded the southern gate")