#Escreva um programa que inverta os caracteres de um string.

def inversor(word):
     lista =list(word)
     lista.reverse()
     return ''.join(lista)
     
     
word = input("Adicione a apalavra: ")
print(inversor(word))