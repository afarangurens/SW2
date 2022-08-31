def validar_numero_digitos(text, new_text):
    if len(new_text) > 4:
        return False
    if len(new_text) == 2:
        if new_text[0] == new_text[1]:
            return False
    if len(new_text) == 3:
        if new_text[0] == new_text[2] or new_text[1] == new_text[2]:
            return False
    if len(new_text) == 4:
        if (new_text[0] == new_text[3] or
           new_text[1] == new_text[3] or new_text[2] == new_text[3]):
            return False
    return text.isdecimal()
