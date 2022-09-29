codigos = [13,20,55,60,70,7,14,33]
cont=0
for codigo in codigos:
    if codigo%2 == 1:
        cont+= 1
print('Há', cont, 'ímpares')