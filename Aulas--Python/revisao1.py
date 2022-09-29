av1 = float(input('Digite a nota da sua Av1:'))
av2 = float (input('Digite a nota da sua Av2:'))
media = (av1+av2)/2

if (media >= 6):
    print('Aprovado!',media)

elif  (media >= 4) and (media <= 5,9):
    print('Final', media)

else:
    print('Reprovado', media)