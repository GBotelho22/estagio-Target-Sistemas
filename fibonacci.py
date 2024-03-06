#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
#ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

import math
i = int(input())

def quadradoperfeito(x):
    s = int(math.sqrt(x))
    return s*s == x
 

def Fibonacci(n):
    return quadradoperfeito(5*n**2 + 4) or quadradoperfeito(5*n**2 - 4)
    

if (Fibonacci(i) == True):
    print (i,"É um número de Fibonacci")
else:
     print (i,"não é um número de Fibonacci")

