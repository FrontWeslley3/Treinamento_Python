
# 🔹 DESAFIO: Criando um sistema de desconto progressivo 💰

# 📌 Enunciado:
# Você foi contratado para desenvolver um sistema de descontos para uma loja online.
# O sistema deve calcular o preço final de um produto com base nos seguintes critérios:
# 1. Se o cliente comprar mais de 10 unidades, recebe um desconto de 10%.
# 2. Se o cliente for um membro VIP, recebe mais 5% de desconto adicional.
# 3. Se o valor final após descontos for maior que R$500, um desconto extra de R$20 é aplicado.

# ✅ Tarefa:
# - Peça ao usuário para inserir o preço unitário do produto.
# - Peça ao usuário para inserir a quantidade desejada.
# - Pergunte se o cliente é VIP (responder com "sim" ou "nao").
# - Calcule o valor final e exiba o total a pagar.

# 🔥 Dica: Utilize operadores aritméticos, lógicos e de comparação para resolver o problema.
# Utilize a função input() para receber os dados do usuário. O default é string, então lembre-se de converter para int ou float caso necessário.
# Exemplo do input: saldo_bancario = float(input("Digite o seu saldo bancario: "))

# ✏️ Comece seu código abaixo:

# Peça ao usuário para inserir o preço unitário do produto (Feito)
preco_unitario = float(input("Digite o Preço do Produto: "))

# Peça ao usuário para inserir a quantidade desejada
quantidade = int(input("Quantidade Desejada: "))

# Pergunte se o cliente é VIP (responder com "sim" ou "nao")  (Feito)
vip = input("Você é VIP? (sim/não): ")

# Calcula o valor total inicial sem desconto  (Feito)
valor_total = preco_unitario * quantidade

# Verifica se a quantidade comprada é maior que 10 para aplicar 10% de desconto   (Feito)
if quantidade > 10:
    desconto = valor_total * 0.10
    valor_total -= desconto

    # Se o cliente for VIP, aplica mais 5% de desconto   (Feito)
    if vip == "sim":
        desconto_vip = valor_total * 0.05
        valor_total -= desconto_vip

# Mostra o valor final a pagar (com ou sem desconto)  (Feito)
print("Valor final a pagar: R$ {:.2f}".format(valor_total))












