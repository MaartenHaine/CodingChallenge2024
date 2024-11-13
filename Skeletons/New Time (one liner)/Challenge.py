"""
As a newspaper editor, you need to validate incoming articles quickly.
Create a one-line input validation that checks each submission.
Requirements:
    Articles must be 256 characters or less,
    use only alphanumeric characters and basic punctuation (. , ! ? ; :),
    and avoid long number sequences (over 10 digits).

example valid article:
    Breaking news: The world is ending in 2012! Read more here.

example invalid article:
    The new study shows that 22222222222 is a prime number.
"""

### INPUT - DO NOT TOUCH
articles = eval(input())
### END INPUT


def validate(message: str) -> bool:
    return False


### OUTPUT - DO NOT TOUCH
print([validate(article) for article in articles])
