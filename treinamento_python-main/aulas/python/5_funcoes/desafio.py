# 🔹 DESAFIO: Criando um Gerador de Tabuada com Funções 📊

# 📌 Enunciado:
# Você foi contratado para desenvolver um programa que gere a tabuada de um número fornecido pelo usuário.
# O sistema deve funcionar da seguinte forma:
# 1. O usuário deve inserir um número inteiro.
# 2. O programa deve exibir a tabuada desse número de 1 a 10.
# 3. Pergunte ao usuário se deseja gerar outra tabuada. Se sim, repita o processo. Caso contrário, finalize o programa.

# ✅ Tarefa:
# - Criar uma função chamada `gerar_tabuada(numero)` que imprime a tabuada de 1 a 10.
# - Utilizar um loop para permitir que o usuário gere várias tabuadas.
# - O programa só deve parar quando o usuário digitar "sair".

# 🔥 Dica:
# - Use a função `input()` para capturar a entrada do usuário.
# - Utilize `while` para repetir até que o usuário deseje sair.
# - Converta a entrada do usuário para `int` antes de calcular a tabuada.

# ✏️ Comece seu código abaixo:


# Função que gera e exibe a tabuada de 1 a 10 para o número informado
def gerar_tabuada(numero):
    # Loop que vai de 1 a 10
    for i in range(1, 11):
        # Exibe o resultado da multiplicação
        print(f"{numero} x {i} = {numero * i}")

# Loop principal que continua até o usuário digitar 'sair'
while True:
    # Solicita ao usuário que digite um número ou o comando 'sair'
    entrada = input("\nDigite um número para ver a tabuada (ou 'sair' para encerrar): ")

    # Se o usuário digitar 'sair', o programa encerra
    if entrada.lower() == "sair":
        print("Programa encerrado. Até a próxima!")
        break  # Sai do loop principal

    # Verifica se a entrada é numérica (evita erro se o usuário digitar letras)
    if entrada.isdigit():
        numero = int(entrada)  # Converte a entrada para inteiro
        print(f"\n🔢 Tabuada do {numero}:")
        gerar_tabuada(numero)  # Chama a função para gerar a tabuada
    else:
        # Caso o usuário digite algo que não é número e nem 'sair'
        print("Por favor, digite um número válido ou 'sair'.")

