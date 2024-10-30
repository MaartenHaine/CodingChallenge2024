"""
As a newspaper editor, you need to validate incoming articles quickly.
Create a one-line input validation that checks each submission.
Requirements:
    Articles must be 256 characters or less,
    use only alphanumeric characters and basic punctuation (. , ! ? ; :),
    and avoid long number sequences (over 10 digits).
hints:
    regex importeren via __import__("re")
"""
### INPUT - DO NOT TOUCH
articles = eval(input())
### END INPUT

def validate(article: str) -> bool:
    return (len(article) <= 256) and all( (char in [".", ",", "!", "?", ";", ":", " "] or char.isalnum()) for char in article) and (lambda article: __import__ ("re").search(r"\d{11,}", article))(article) is None

### OUTPUT - DO NOT TOUCH
print([validate(article) for article in articles])