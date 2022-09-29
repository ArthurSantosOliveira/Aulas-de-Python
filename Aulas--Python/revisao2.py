contador = 0 
contador2 = 0
while (contador < 15):
    idade=int(input('Digite sua idade:'))
    if (idade >=20) or (idade <= 30):
        contador2+=1
    contador+=1

print('Há', contador2, 'pessoas com idade entre 20 e 30')