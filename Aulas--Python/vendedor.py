cod = input("Escolha o código do produto: 1001, 1234, 6548, 0987, 7632: \n")
quantidade = int(input("Digite a quantidade do produto que deseja: "))

if(cod == '1001'):
    valor = 5.32 * quantidade
    print("O preço total é R$",valor)

if(cod == '1234'):
    valor = 6.45 * quantidade
    print("O preço total é R$",valor)

if(cod == '6548'):
    valor = 2.37 * quantidade
    print("O preço total é R$",valor)
    
if(cod == '0987'):
    valor = 5.32 * quantidade
    print("O preço total é R$",valor)

if(cod == '7632'):
    valor = 6.45 * quantidade
    print("O preço total é R$",valor)
