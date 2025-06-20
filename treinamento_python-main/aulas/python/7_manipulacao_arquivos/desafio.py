# 🔹 DESAFIO: Gerenciador de Notas 📂

# 📌 Enunciado:
# Você foi contratado para desenvolver um programa que gerencie notas em um arquivo de texto.
# O sistema deve funcionar da seguinte forma:
# 1. O usuário pode escolher entre adicionar uma nova nota ou visualizar todas as notas salvas.
# 2. Se o usuário escolher adicionar, ele deve inserir um título e um conteúdo para a nota.
# 3. As notas devem ser salvas em um arquivo chamado "notas.txt", com cada nota separada por uma linha.
# 4. Se o usuário escolher visualizar, o programa deve exibir todas as notas armazenadas.
# 5. O programa só deve parar quando o usuário digitar "sair".

# ✅ Tarefa:
# - Criar uma função chamada `adicionar_nota(titulo, conteudo)` para salvar a nota no arquivo.
# - Criar uma função chamada `visualizar_notas()` para exibir todas as notas armazenadas.
# - Utilizar um loop para permitir múltiplas interações com o usuário.
# - O programa só deve parar quando o usuário digitar "sair".

# 🔥 Dica:
# - Use a função `open("notas.txt", "a")` para adicionar uma nova nota sem apagar as anteriores.
# - Use `open("notas.txt", "r")` para ler e exibir todas as notas.
# - Utilize `strip()` para remover espaços extras ao ler o arquivo.
# - Use `while` para repetir até que o usuário deseje sair.

# ✏️ Comece seu código abaixo:

# Função para adicionar uma nota
def adicionar_nota(titulo, conteudo):
  with open("notas.txt", "a") as arquivo:
    arquivo.write(f"{titulo}: {conteudo}\n")

# Função para visualizar notas
def visualizar_notas():
  with open("notas.txt", "r") as arquivo:
    notas = arquivo.readlines()
    for nota in notas:
      print(nota.strip())

# Loop principal
while True:
  print("1. Adicionar nota")
  print("2. Visualizar notas")
  print("3. Sair")
  escolha = input("Escolha uma opção: ")
  if escolha == "1":
    titulo = input("Digite o título da nota: ")
    conteudo = input("Digite o conteúdo da nota: ")
    adicionar_nota(titulo, conteudo)
  elif escolha == "2":
    visualizar_notas()
  elif escolha == "3":
    break
  else:
    print("Opção inválida. Tente novamente.")

