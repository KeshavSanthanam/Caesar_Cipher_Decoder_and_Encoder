import sys


class VigenereCipher:
    def __init__(self):
        self.key = ""

    def set_key(self, key):
        self.key = key

    def encrypt(self, e_text):
        if not self.key:
            return "ERROR Password not set"

        e_out = ""
        key_length = len(self.key)
        for i in range(len(e_text)):
            c = e_text[i]
            if c.isalpha():
                key_c = self.key[i % key_length]
                shift = ord(key_c.upper()) - ord('A')
                if c.isupper():
                    encrypted_c = chr(((ord(c) - ord('A') + shift) % 26) + ord('A'))
                else:
                    encrypted_c = chr(((ord(c) - ord('a') + shift) % 26) + ord('a'))
                e_out += encrypted_c
            else:
                e_out += c
        return "RESULT " + e_out

    def decrypt(self, d_text):
        if not self.key:
            return "ERROR Password not set"
        d_out = ""
        for i in range(len(d_text)):
            c = d_text[i]
            if c.isalpha():
                key_c = self.key[i % len(self.key)]
                shift = ord(key_c.upper()) - ord('A')
                if c.isupper():
                    decrypted_c = chr(((ord(c) - ord('A') - shift) % 26) + ord('A'))
                else:
                    decrypted_c = chr(((ord(c) - ord('a') - shift) % 26) + ord('a'))
                d_out += decrypted_c
            else:
                d_out += c
        return "RESULT " + d_out


def main():
    cipher = VigenereCipher()
    while True:
        command = input()
        parts = command.split(None, 1)
        if not parts:
            continue
        arg = parts[1] if len(parts) > 1 else ""
        if parts[0] == "PASSKEY":
            cipher.set_key(arg)
            print("RESULT")
        elif parts[0] == "ENCRYPT":
            result = cipher.encrypt(arg)
            print(result)
        elif parts[0] == "DECRYPT":
            result = cipher.decrypt(arg)
            print(result)
        elif parts[0] == "QUIT":
            break
        else:
            print("ERROR Invalid command")


if __name__ == "__main__":
    main()
