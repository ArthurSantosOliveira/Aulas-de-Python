contador = 0 
contador2 = 0
contadorPorcentagem = 0
somaIdade = 0
while(contador < 2):
    idade=int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    somaIdade = somaIdade + idade
    media1 = somaIdade/10
    contador+=1
    if (idade >=18):
        contador2+=1
    if ( (idade>18 and idade < 30 and altura > 1.8) ):
        contadorPorcentagem +=1

porcentagem = contadorPorcentagem/100

print ('A média da idade do grupo é:', media1)
print('Há', contador2, 'pessoa(s) maior(es) de idade')
print(porcentagem)