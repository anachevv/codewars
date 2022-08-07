def alphabet_position(text):
    return " ".join(str(ord(character) - 96) for character in text.lower() if character.isalpha())
