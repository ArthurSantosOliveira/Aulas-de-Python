contador = 0 
contador2 = 0
somaIdade = 0
while(contador < 10):
    idade=int(input('Digite sua idade:'))
    somaIdade = somaIdade + idade
    media1 = somaIdade/10
    contador+=1
    if (idade >=18):
        contador2+=1
   
print ('A média da idade do grupo é:', media1)
print('Há', contador2, 'pessoa(s) maior(es) de idade')