from cipher import decrypt

def brute_force_attack(cipher_text):
    possibilities = {}

    for key in range(1, 26):
        possibilities[key] = decrypt(cipher_text, key)

    return possibilities
