from cipher import encrypt, decrypt
from brute_force import brute_force_attack
from utils import validate_key, validate_text

def main():
    print("\n=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute-force Decrypt")

    choice = input("Choose option (1/2/3): ")

    try:
        if choice in ['1', '2']:
            text = validate_text(input("Enter text: "))
            key = validate_key(input("Enter key (1-25): "))

            if choice == '1':
                print("Encrypted Text:", encrypt(text, key))
            else:
                print("Decrypted Text:", decrypt(text, key))

        elif choice == '3':
            text = validate_text(input("Enter encrypted text: "))
            results = brute_force_attack(text)

            print("\nPossible decryptions:")
            for k, v in results.items():
                print(f"Key {k}: {v}")

        else:
            print("Invalid option selected")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
