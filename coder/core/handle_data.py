def encoding(characters: str):
    encoded = ""
    encoded += str(ord(characters[0]))
    for i in range(1, len(characters)):
        previous = i - 1
        encoded += " " + str(ord(characters[i]) - ord(characters[previous]))

    return encoded

def decoding(character_codes: str):
    character_codes = character_codes.split()
    char_value = int(character_codes[0])
    decoded = chr(int(character_codes[0]))

    for i in range(1, len(character_codes)):
        char_value += int(character_codes[i])
        decoded += chr(char_value)

    return decoded