idade = int(input("digite sua idade "))
idade__dias = idade * 365
idade__horas = idade__dias * 24
txt = "Você ja viveu {} dias, isso significa {} horas. "
print(txt.format(idade__dias, idade__horas))