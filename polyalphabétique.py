
def chiffrer(texte, decalage):
    texte_chiffre = ""
    decalage = int(decalage)
    for char in texte:
        if char.isalpha():
            if char.isupper():
                texte_chiffre += chr((ord(char) + decalage - 65) % 26 + 65)
            else:
                texte_chiffre += chr((ord(char) + decalage - ord('a')) % 26 + ord('a'))
        else:
            texte_chiffre += char

    return texte_chiffre

def dechiffrer(texte_chiffre, decalage):
    texte_dechiffre = ""

    for char in texte_chiffre:
        if char.isalpha():
            if char.isupper():
                texte_dechiffre += chr((ord(char) - decalage - ord('A')) % 26 + ord('A'))
            else:
                texte_dechiffre += chr((ord(char) - decalage - ord('a')) % 26 + ord('a'))
        else:
            texte_dechiffre += char

    return texte_dechiffre