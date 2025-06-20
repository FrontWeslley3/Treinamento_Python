# 🔹 DESAFIO: Analisador de Texto 📄

# 📌 Enunciado:
# Você foi contratado para desenvolver um programa que analise um texto fornecido pelo usuário.
# O sistema deve funcionar da seguinte forma:
# 1. O usuário deve inserir um texto qualquer.
# 2. O programa deve exibir:
#    - Quantidade de palavras no texto.
#    - Quantidade de caracteres (sem contar espaços).
#    - A palavra mais longa do texto.
# 3. Pergunte ao usuário se deseja analisar outro texto. Se sim, repita o processo. Caso contrário, finalize o programa.

# ✅ Tarefa:
# - Criar uma função chamada `analisar_texto(texto)` que exibe as informações pedidas.
# - Utilizar um loop para permitir que o usuário analise vários textos.
# - O programa só deve parar quando o usuário digitar "sair".

# 🔥 Dica:
# - Use a função `input()` para capturar a entrada do usuário.
# - Utilize `split()` para dividir o texto em palavras.
# - Utilize `max()` com a função `key=len` para encontrar a palavra mais longa.
# - Use `while` para repetir até que o usuário deseje sair.

# ✏️ Comece seu código abaixo:

def analisar_texto(texto):
  palavras = texto.split()
  quantidade_palavras = len(palavras)

  quantidade_caracteres = len(texto.replace(" ", ""))

  palavra_mais_longa = max(palavras, key = len)

  print(f"Quantidade de palavras: {quantidade_palavras}")
  print(f"Quantidade de caracteres: {quantidade_caracteres}")
  print(f"Palavra mais longa: {palavra_mais_longa}")

  return

while True:
  texto = input("Digite um texto:")

  if texto.lower() == "sair":
    break

  analisar_texto(texto)


  continuar = input("Deseja analiar outro texto? (sim/não):")
  if continuar.lower() == "não":
    break

