"""
As a newspaper editor, you need to validate incoming articles quickly.
Create a one-line input validation that checks each submission.
Requirements:
    Articles must be 256 characters or less,
    use only alphanumeric characters and basic punctuation (. , ! ? ; :),
    and avoid long number sequences (over 10 digits).
"""

### INPUT - DO NOT TOUCH
articles = eval(input())
### END INPUT


def validate(message: str) -> bool:
    return False


### OUTPUT - DO NOT TOUCH
print([validate(article) for article in articles])
