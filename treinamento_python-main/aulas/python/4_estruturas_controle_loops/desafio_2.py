# ✅ Desafio 2: Jogo de Adivinhação Simples
# 📌 Enunciado:
# Crie um programa onde o usuário deve adivinhar um número entre 1 e 10. O programa deve continuar solicitando tentativas até que o usuário acerte.

# Depois de acertar, pergunte se deseja jogar novamente ou sair.

# ✨ Regras:
# O número secreto pode ser fixo (ex: 7).

# Se acertar, diga “Você acertou!”.

# Se errar, diga “Tente novamente!”.

# Após acerto, pergunte: "Deseja jogar novamente? (sim/sair):"



numero_secreto = 7  # número fixo para adivinhação

while True:
    while True:
        tentativa = int(input("Adivinhe o número entre 1 e 10: "))
        if tentativa == numero_secreto:
            print("Você acertou!")
            break
        else:
            print("Tente novamente!")

    continuar = input("Deseja jogar novamente? (sim/sair): ").lower()
    if continuar == "sair":
        print("Obrigado por jogar!")
        break