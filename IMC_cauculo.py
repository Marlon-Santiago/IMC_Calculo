nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')
altura = input('Qual a sua altura: ')
ano_atual = input('Qual o ano atual: ')
idade = int(idade)
ano_atual = int(ano_atual)
ano_naicimente = ano_atual - idade
peso = int(peso)
altura = float(altura)
imc = peso / altura ** 2
abaixo_peso = 18.5
peso_normal = 18.6
peso_normal2 = 24.9
acima_peso = 25
acima_peso2 = 29.9
obesidade = 30
obesidade1 = 34.9
obesidade2 = 35
obesidade_2 = 39.9
obesidade3 = 40


if imc <= abaixo_peso:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} com {peso}KG e abaixo do peso ideal ')

elif imc >= peso_normal and imc <= peso_normal2:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e no peso ideal ')

elif imc >= acima_peso and imc <= acima_peso2:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e acima do peso ideal ')

elif imc >= obesidade and imc <= obesidade1:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 1 ')

elif imc >= obesidade2 and imc <= obesidade_2:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 2 ')

else:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 3 ')

