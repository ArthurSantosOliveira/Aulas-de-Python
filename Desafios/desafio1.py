#input que vai receber o valor da piramide
# #h = altura
h = int(input("altura piramide de 1 a 8: "))

#laco de repeticao para que o numero inserido seja entre 1 e 8 
while h > 8:
    h = int(input("altura piramide de 1 a 8: "))

#loop que ira criar as duas piramides, onde 'i' quantidade de (#)  'printadas' dentro do comprimento da variavel e 'h' eh a altura inserida pelo usuário 
for i in range(h): 
    j = i + 1
    print(" " * (h - i) + "#" * (i + 1) + " " + ("#" * j ))
    
