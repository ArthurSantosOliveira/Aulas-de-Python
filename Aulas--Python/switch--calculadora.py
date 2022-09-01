x = int(input('1:Soma, 2:Subtração, 3:Multiplicação, 4:Divisão '))
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
print({
        1 : lambda x: num1 + num2,
        2 : lambda x: num1 - num2,
        3 : lambda x: num1 * num2,
        4 : lambda x: num1 / num2                    
    }[x](num1))