def validate_key(key):
    if not key.isdigit():
        raise ValueError("Key must be a number")
    key = int(key)
    if key < 1 or key > 25:
        raise ValueError("Key must be between 1 and 25")
    return key


def validate_text(text):
    if not text.strip():
        raise ValueError("Text cannot be empty")
    return text
