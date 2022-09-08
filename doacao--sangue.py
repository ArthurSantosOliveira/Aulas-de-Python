nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if (idade < 18):
    print(nome + " você não deve doar porque é menor")
elif (idade >= 18 and peso < 50):
    print(nome," Você é maior mas não tem peso suficiente")
else:
    print("Você pode doar sangue")
