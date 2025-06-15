# 🔹 DESAFIO: Criando um Sistema de Gestão de Veículos 🚗

# 📌 Enunciado:
# A concessionária "Super Carros" deseja um sistema para gerenciar seu estoque de veículos
# utilizando Programação Orientada a Objetos (POO). O sistema deve permitir o cadastro,
# listagem, edição e remoção de veículos.
#
# O sistema deve funcionar da seguinte forma:
# 1. O usuário pode cadastrar um novo veículo informando:
#    - Marca
#    - Modelo
#    - Ano
#    - Tipo (Carro, Moto, Caminhão) *(se nenhum tipo for informado corretamente, o padrão será Carro)*.
# 2. O usuário pode visualizar a lista de veículos cadastrados.
# 3. O usuário pode editar os dados de um veículo existente.
# 4. O usuário pode remover um veículo pelo índice da lista.
# 5. O sistema deve rodar em um loop até que o usuário escolha sair.

# ✅ Tarefa:
# - Criar uma classe `Veiculo` com atributos `marca`, `modelo` e `ano`.
# - Criar classes `Carro`, `Moto` e `Caminhao`, que herdam de `Veiculo` e adicionam um atributo `tipo`.
# - Criar uma classe `Concessionaria` que gerencia a lista de veículos.
# - Implementar métodos para cadastrar, listar, editar e remover veículos.
# - Criar um menu interativo para o usuário.
#
# 🔥 Dica:
# - Utilize listas para armazenar os veículos.
# - Use `input()` para interagir com o usuário.
# - Utilize herança para diferenciar os tipos de veículos.
# - Certifique-se de tratar entradas inválidas.

# Classe base Veiculo

class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def exibir_dados(self):
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Ano: {self.ano}")


class Carro(Veiculo):
  def __init__(self, marca, modelo, ano):
    super().__init__(marca, modelo, ano)
    self.tipo = "Carro"

  def exibir_dados(self):
    super().exibir_dados()
    print(f"Tipo: {self.tipo}")


class Moto(Veiculo):
  def __init__(self, marca, modelo, ano):
    super().__init__(marca, modelo, ano)
    self.tipo = "Moto"

  def exibir_dados(self):
    super().exibir_dados()
    print(f"Tipo: {self.tipo}")


class Caminhao(Veiculo):
  def __init__(self, marca, modelo, ano):
    super().__init__(marca, modelo, ano)
    self.tipo = "Caminhao"

  def exibir_dados(self):
    super().exibir_dados()
    print(f"Tipo: {self.tipo}")


class Concessionaria:
  def __init__(self):
    self.veiculos = []

  def cadastrar_veiculo(self):
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    tipo = input("Digite o tipo do veículo (Carro, Moto, Caminhao): ")

    if tipo == "Carro":
      veiculo = Carro(marca, modelo, ano)
    elif tipo == "Moto":
      veiculo = Moto(marca, modelo, ano)
    elif tipo == "Caminhao":
      veiculo = Caminhao(marca, modelo, ano)
    else:
      print("Tipo de veículo inválido.")
      return

    self.veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso.")

  def listar_veiculos(self):
    for i, veiculo in enumerate(self.veiculos):
      print(f"Veículo {i+1}:")
      veiculo.exibir_dados()
      print()

  def editar_veiculo(self):
    indice = int(input("Digite o índice do veículo que deseja editar: ")) - 1
    if indice < 0 or indice >= len(self.veiculos):
      print("Índice inválido.")
      return

    veiculo = self.veiculos[indice]
    marca = input("Digite a nova marca do veículo: ")
    modelo = input("Digite o novo modelo do veículo: ")
    ano = input("Digite o novo ano do veículo: ")

    veiculo.marca = marca
    veiculo.modelo = modelo
    veiculo.ano = ano

    print("Veículo editado com sucesso.")

  def remover_veiculo(self):
    indice = int(input("Digite o índice do veículo que deseja remover: ")) - 1
    if indice < 0 or indice >= len(self.veiculos):
      print("Índice inválido.")
      return

    del self.veiculos[indice]
    print("Veículo removido com sucesso.")


def main():
  concessionaria = Concessionaria()

  while True:
    print("1. Cadastrar veículo")
    print("2. Listar veículos")
    print("3. Editar veículo")
    print("4. Remover veículo")
    print("5. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
      concessionaria.cadastrar_veiculo()
    elif opcao == "2":
      concessionaria.listar_veiculos()
    elif opcao == "3":
      concessionaria.editar_veiculo()
    elif opcao == "4":
      concessionaria.remover_veiculo()
    elif opcao == "5":
      print("Saindo do programa.")
      break
    else:
      print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
  main()