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


def validate(message: str) -> bool:
    return (message.isalnum() and len(message) <= 256) and all( char in ".,!?;:".split() or char.isalnum() for char in message) and (lambda message: __import__ ("re").search(r"\d{11,}", message))(message) is None
