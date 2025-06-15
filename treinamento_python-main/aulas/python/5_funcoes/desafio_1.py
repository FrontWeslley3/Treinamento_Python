'''
🔹 Desafio: Gerador de Potências com Funções

📌 Enunciado:
Crie um programa em Python que:

- Peça ao usuário um número inteiro positivo.
- Calcule e exiba a potência desse número de 1 a 10 (ou seja: n¹, n², n³ ... até n¹⁰).
- Use uma função chamada mostrar_potencias(numero) para mostrar as potências.
- O programa só deve parar quando o usuário digitar "sair".
'''

# Função responsável por exibir as potências do número recebido
def mostrar_potencias(numero):
    '''
    Esta função recebe um número inteiro positivo como parâmetro
    e exibe sua potência de 1 até 10.

    Exemplo de saída para número = 2:
    2 ^ 1 = 2
    2 ^ 2 = 4
    2 ^ 3 = 8
    ...
    2 ^ 10 = 1024
    '''
    for i in range(1, 11):
        print(f"{numero} ^ {i} = {numero ** i}")

# Loop principal do programa
while True:
    # Solicita ao usuário que digite um número inteiro positivo ou "sair" para encerrar o programa
    numero = input("Digite um número inteiro positivo ou 'sair' para encerrar: ")

    # Verifica se o usuário deseja sair do programa
    if numero.lower() == "sair":
        break  # Encerra o loop e finaliza o programa

    try:
        # Converte a entrada para inteiro
        numero = int(numero)

        # Verifica se o número é positivo
        if numero > 0:
            # Chama a função para exibir as potências
            mostrar_potencias(numero)
        else:
            # Caso o número seja zero ou negativo, exibe uma mensagem de aviso
            print("Por favor, digite um número inteiro positivo.")
    except ValueError:
        # Trata o erro caso a conversão para inteiro falhe (entrada inválida)
        print("Entrada inválida. Por favor, digite um número inteiro.")
