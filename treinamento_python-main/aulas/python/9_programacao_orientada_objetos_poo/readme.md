# 🚗 Sistema de Gestão de Veículos - Super Carros 🚙

## 📌 Sobre o Projeto

Este é um sistema simples desenvolvido em **Python** utilizando **Programação Orientada a Objetos (POO)** para gerenciar o estoque de uma concessionária fictícia chamada **Super Carros**.

O sistema permite:

- ✅ Cadastro de veículos
- ✅ Listagem de veículos cadastrados
- ✅ Edição de informações de veículos
- ✅ Remoção de veículos
- ✅ Menu interativo para o usuário final

---

## ✅ Funcionalidades

- Cadastrar veículos com:
  - Marca
  - Modelo
  - Ano
  - Tipo (Carro, Moto ou Caminhão)
- Listar todos os veículos cadastrados com detalhes.

- Editar informações de um veículo específico pelo índice da lista.

- Remover um veículo pelo índice.

- Sistema roda em loop até o usuário escolher **"Sair"**.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Paradigma:** Programação Orientada a Objetos (POO)

---

## 🗃️ Estrutura de Classes

- **Classe Base:**

  - `Veiculo` (atributos: marca, modelo, ano)

- **Subclasses (herança):**
  - `Carro`
  - `Moto`
  - `Caminhao`

Cada tipo de veículo tem um atributo específico chamado `tipo`.

- **Classe de Controle:**
  - `Concessionaria`  
    Responsável por gerenciar a lista de veículos e oferecer métodos para:

✅ Cadastrar  
✅ Listar  
✅ Editar  
✅ Remover

---

## 🚀 Como Executar o Projeto

### 📍 Pré-requisitos:

- Ter o **Python 3.x** instalado na sua máquina.

### 📍 Passos:

1. Clone o repositório ou baixe os arquivos:

```bash
git clone https://github.com/FrontWeslley3/sistema-gestao-veiculos.git
```
