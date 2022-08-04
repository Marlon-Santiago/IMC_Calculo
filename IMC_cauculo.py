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



if imc <= 18.5:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} com {peso}KG e abaixo do peso ideal ')

elif imc >= 18.6 and imc <= 24.9:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e no peso ideal ')

elif imc >= 25 and imc <= 29.9:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e acima do peso ideal ')

elif imc >= 30 and imc <= 34.9:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 1 ')

elif imc >= 35 and imc <= 39.9:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 2 ')

else:
    print(f'{nome} tem {idade} anos nasceu em {ano_naicimente} está com o imc {imc:.2f} e com obesidade nivel 3 ')

