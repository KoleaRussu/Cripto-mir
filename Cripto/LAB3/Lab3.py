def remove_spaces(text):
    return text.replace(" ", "")

def format_input(text):
    text = text.upper()
    text = remove_spaces(text)
    return text

def vigenere(text, key, decrypt=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = format_input(key)

    result = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        if char in alphabet:
            if decrypt:
                offset = alphabet.index(char) - alphabet.index(key[key_index])
            else:
                offset = alphabet.index(char) + alphabet.index(key[key_index])

            offset %= len(alphabet)
            result += alphabet[offset]

            key_index = (key_index + 1) % key_length
        else:
            result += char

    return result

def main():
    operation = input("Выберите операцию (шифрование/дешифрование): ").lower()
    key = input("Введите ключ (как минимум 7 символов): ")
    if len(key) < 7:
        print("Ключ должен содержать как минимум 7 символов.")
        return

    message = input("Введите сообщение или шифртекст: ")

    if operation == "шифрование":
        result = vigenere(message, key)
        print("Шифртекст:", result)
    elif operation == "дешифрование":
        result = vigenere(message, key, decrypt=True)
        print("Дешифрованное сообщение:", result)
    else:
        print("Неизвестная операция. Выберите шифрование или дешифрование.")

if __name__ == "__main__":
    main()
