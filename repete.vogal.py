words = []
while True:
    word =  input("Digite uma palavra (ou enter para sair):").strip()
    if not word: # condição de parada
        break
    
    final_word = ""
    for letter in word:
        # TODO: Remover acentuação usando função
        if letter.lower() in "aeiouãêóíá": 
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*word, sep="\n")