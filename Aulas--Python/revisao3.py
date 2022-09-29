n = float(input('Digite um número:'))

maiorValor = n
contador=0

while (n != 0):
    n = float(input('Digite um número:'))
    
    if(n > maiorValor):
        maiorValor = n
        
print("O maior valor é: ", maiorValor)    