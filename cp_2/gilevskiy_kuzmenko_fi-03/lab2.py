alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
p = [0.0721, 0.0154, 0.0411, 0.0179, 0.0322, 0.0836, 0.0913, 0.0259, 0.0703, 0.0012, 0.0181, 0.0517, 0.0348, 0.0654,
     0.1092, 0.0274, 0.0466, 0.0563, 0.0635, 0.0251, 0.0034, 0.0086, 0.0043, 0.0132, 0.0082, 0.0071, 0.0441, 0.0332,
     0.0746, 0.0213, 0.0015, 0.0052]


def clean_text(text):
    cleaned_text = ""
    for char in text.upper():
        if char in alphabet:
            cleaned_text += char

    return cleaned_text


def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        key_char = key[key_index % key_length]
        key_index += 1

        encrypted_index = (alphabet.index(char) + alphabet.index(key_char)) % 32
        encrypted_char = alphabet[encrypted_index]

        ciphertext += encrypted_char

    return ciphertext


def calculate_index_of_coincidence(text):
    text_length = len(text)
    frequencies = [0] * 32
    for char in text:
        frequencies[alphabet.index(char)] += 1

    ioc = sum([(f * (f - 1)) / (text_length * (text_length - 1)) for f in frequencies])

    return ioc


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        key_char = key[key_index % key_length]
        key_index += 1

        decrypted_index = (alphabet.index(char) - alphabet.index(key_char)) % 32
        decrypted_char = alphabet[decrypted_index]

        plaintext += decrypted_char

    return plaintext


def divide_blocks(text, r):
    blocks = []
    for i in range(r):
        block = text[i::r]
        blocks.append(block)
    return blocks


def key_len(text):
    k_len = {}
    for k in range(2, 32):
        i = 0
        blocks = divide_blocks(text, k)
        for b in blocks:
            i += calculate_index_of_coincidence(b)
        i = i / len(blocks)
        k_len[k] = i
    return max(k_len, key=k_len.get)


def find_key_with_Mg_method(text, r):
    key = ""
    blocks = divide_blocks(text, r)
    for i in range(r):
        k = 0
        M = 0
        for g in range(32):
            tempM = 0
            for t in range(32):
                tempM += p[t] * blocks[i].count(alphabet[(t + g) % 32])
            if tempM > M:
                M = tempM
                k = g
        key += alphabet[k]
    return key


def main():
    with open("text.txt", "r") as file:
        plaintext = clean_text(file.read())

    keys = {
        'key2': 'ок',
        'key3': 'лан',
        'key4': 'рофл',
        'key5': 'кебаб',
        'key10': 'омегалулыч'
    }

    encrypted_texts = {}
    iocs = {}

    for key_name, key_value in keys.items():
        encrypted_text = vigenere_encrypt(plaintext, key_value.upper())
        encrypted_texts[key_name] = encrypted_text

        ioc = calculate_index_of_coincidence(encrypted_text)
        iocs[key_name] = ioc

    print("Індекс відповідності:")
    print(f"Відкритий текст: {calculate_index_of_coincidence(plaintext)}")
    for key_name, ioc_value in iocs.items():
        print(f"Зашифрований текст за ключем {key_name}: {ioc_value}")

    with open("CipherText.txt", "r") as file:
        ciphertext = clean_text(file.read().upper())

    key_length = key_len(ciphertext)
    print("Key length:" + str(key_length))

    key = find_key_with_Mg_method(ciphertext, key_length)
    print("Key:" + key)

    file = open("result.txt", "w")
    file.write(vigenere_decrypt(ciphertext, key))
    file.close()


if __name__ == '__main__':
    main()
