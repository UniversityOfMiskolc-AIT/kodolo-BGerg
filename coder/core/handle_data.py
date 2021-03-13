def encoding(characters: str):
    encoded = ""
    encoded += str(ord(characters[0]))
    for i in range(1, len(characters)):
        previous = i - 1
        encoded += " " + str(ord(characters[i]) - ord(characters[previous]))

    return encoded

def decoding(character_codes: list):
    character_codes = character_codes.split()
    char_value = int(character_codes[0])
    decoded = chr(char_value)

    if len(character_codes) > 1:
        for i in range(1, len(character_codes)):
            char_value += int(character_codes[i])
            decoded += chr(char_value)

    return decoded

def validate_to_encoding(characters: str):
    if characters.isascii():
        pass
    else:
        raise TypeError("Input can only contain ASCII characters for encoding")

def validate_to_decoding(character_codes: str):
    values = character_codes.split()
    for elem in values:
        if elem.isnumeric() and int(elem) <= 127:
            pass
        else:
            raise TypeError("Input can only contain ASCII character numbers for decoding")