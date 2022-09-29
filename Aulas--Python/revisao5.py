contador = 0 
contador2 = 0
while(contador < 10):
    idade=int(input('Digite sua idade:'))
    if (idade >=18):
        contador2+=1
    contador+=1

print('Há', contador2, 'pessoa(s) maior(es) de idade')
