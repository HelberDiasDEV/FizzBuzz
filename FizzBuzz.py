import os
os.system('cls')

def FizzBuzz(k):
    resultado = ''
    for i in range(1, k + 1):
        if i%3 == 0:
            resultado += 'FIZZ'
        if i%5 == 0:
            resultado += 'BUZZ'
        if i%3 != 0 and i%5 != 0:
            resultado += str(i)
        resultado += ' '
    return resultado.strip()
        
    
assert FizzBuzz(3) == "1 2 FIZZ", "Falhou no teste 1"
assert FizzBuzz(5) == "1 2 FIZZ 4 BUZZ", "Falhou no teste 2"
assert FizzBuzz(10) == "1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ", "Falhou no teste 3"
assert FizzBuzz(16) == "1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ 16", "Falhou no teste 3"


