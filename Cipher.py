def encrypt(text, key):
    result = []
    key = key % 26  # dynamic key normalization

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + key) % 26 + base)
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)


def decrypt(text, key):
    return encrypt(text, -key)
