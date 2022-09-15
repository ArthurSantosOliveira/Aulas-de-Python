valor1 = float(input("Digite o valor de a: "))
valor2 = float(input("Digite valor de b: "))
valor3 = float(input("Digite o valor de c: "))

maiorValor = valor1

txt = "Os valores digitados foram A: {}, B: {}, C: {}"

print(txt.format(valor1,valor2,valor3))

if(maiorValor < valor2):
    maiorValor = valor2
    print("O maior valor é B: ",maiorValor)

if (maiorValor < valor3):
    maiorValor = valor3
    print("O maior valor é C: ",maiorValor)

if(maiorValor > valor2 > valor3):
    print("O maior valor é A: ", maiorValor)
