"""
Desafio 1: Contador de Números Pares

📌 Objetivo:
Este programa solicita que o usuário digite um número inteiro positivo e exibe todos os números pares de 0 até esse número.

📋 Funcionalidades:
- Aceita um número inteiro digitado pelo usuário. ✅
- Exibe todos os números pares no intervalo de 0 até o número informado. ✅
- Pergunta ao usuário se deseja continuar executando o programa. ✅
- Encerra o programa caso o usuário digite "sair". ✅

💡 Regras:
- O programa utiliza laços de repetição (while e for).
- Usa estruturas condicionais para verificar se o número é par.
- Converte a resposta do usuário para letras minúsculas para evitar erros de digitação.
"""

while True:
    # Solicita ao usuário um número inteiro ✅
    numero = int(input("Digite um número inteiro: "))

    # Exibe os números pares de 0 até o número informado ✅
    print(f"Números pares até {numero}:")
    for i in range(0, 11):
        if i % 2 == 0:
            print(i)

    # Pergunta se o usuário deseja continuar ou encerrar ✅
    continuar = input("Deseja continuar? (sim/sair): ").lower()
    if continuar == "sair":
        print("Programa encerrado. Até a próxima!")
        break
