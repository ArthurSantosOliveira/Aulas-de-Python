nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade ')) 

anoatual = 2022
anonasci = 2022 - idade

txt='bom dia {}, você nasceu em {}'

print(txt.format(nome, anonasci))