from collections import Counter

texto = input('Digite um texto: ')

palavras = texto.split()
quantidade_palavras = len(palavras)

letras = texto.replace(' ','')
num_letras = len(letras)   

print(f'O texto contém {quantidade_palavras} palavras.')

print(f'O texto possui {num_letras} letras.')

palavra_mais_frequente = Counter(palavras.lower())

print(palavra_mais_frequente)