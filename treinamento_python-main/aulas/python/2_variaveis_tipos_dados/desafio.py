# 🏆 DESAFIO: Manipulação de Variáveis e Tipos de Dados

# Objetivo: O aluno deve corrigir e completar o código abaixo para que ele funcione corretamente.
# O programa deve armazenar informações de um usuário, processá-las e exibir uma mensagem personalizada.

# 📝 Instruções:
# 1. Defina corretamente as variáveis abaixo preenchendo os valores adequados.
# 2. Converta os tipos de dados conforme necessário para realizar os cálculos e concatenar as strings corretamente.
# 3. Substitua os '???' pelas expressões corretas.
# 4. Execute o código e veja se a saída está correta (abra o terminal, execute o comando python > arquivo).

# Definição de variáveis
nome = 'Weslley'  # Nome do usuário (string)
idade = 28  # Idade do usuário (int)
altura = 1.85  # Altura do usuário (float)
peso = 87.5  # Peso do usuário (float)

# Cálculo do IMC (Índice de Massa Corporal)
imc = peso / (altura ** 2)

# Verifica a classificação do IMC (Índice de Massa Corporal) com base no valor calculado:

if imc < 18.5:
    # Se o IMC for menor que 18.5, significa que a pessoa está abaixo do peso ideal
    classificacao = "abaixo do peso"

elif imc >= 18.5 and imc <= 24.9:
    # Se o IMC estiver entre 18.5 e 24.9 (inclusive), a pessoa está com peso normal
    classificacao = "Peso normal"

else:
    # Se o IMC for maior que 24.9, a pessoa está com sobrepeso
    classificacao = "Sobrepeso"


# Perguntar a comida favorita do usuário
comida_favorita = input("Qual é a sua comida favorita? ")


# Mensagem formatada usando f-string
mensagem = f"Olá, {nome}! Você tem {idade} anos, mede {altura}m e pesa {peso}kg."
mensagem_imc = f"Seu IMC é {imc:.2f}.  O que significa que você está {classificacao}."


# Exibir resultados
print(mensagem)
print(mensagem_imc)
print(f"E é muito bom saber que sua comida favorita é {comida_favorita}!")


# Desafio extra:
# 1. Modifique o programa para classificar o IMC como "Abaixo do peso", "Peso normal" ou "Sobrepeso".
# 2. Pergunte ao usuário qual é a sua comida favorita e exiba uma mensagem incluindo essa informação.
