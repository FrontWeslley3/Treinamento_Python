# 🍿 Exercício de Treino – Desconto no Combo de Cinema

# 📌 Enunciado:
# Você está desenvolvendo um sistema para calcular o valor final de uma compra de combos no cinema. ✅ 
# O sistema deve aplicar os seguintes critérios:
# - Se o cliente comprar mais de 5 combos, ele recebe 8% de desconto. ✅ 
# - Se o cliente for estudante, recebe mais 10% de desconto adicional. ✅ 
# - Se o valor final (após os descontos) for acima de R$200, aplica-se um desconto fixo de R$15 no total. ✅ 

# Solicite o preço de um combo. ✅ 
preco_combo = float(input("Digite o Valor do Combo: "))

# Solicite a quantidade de combos. ✅ 
quantidade_combo = int(input("Quantos combos você deseja? "))

# Pergunte se o cliente é estudante (responder com "sim" ou "não"). ✅ 
estudante = input("Você é Estudante? (sim/não): ").strip().lower()

# Calcule o valor total sem desconto
valor_total_combo = preco_combo * quantidade_combo

# Aplica desconto para mais de 5 combos ✅ 
if quantidade_combo > 5:
    desconto = valor_total_combo * 0.08
    valor_total_combo -= desconto

# Aplica desconto adicional para estudante ✅ 
if estudante == "sim":
    desconto_estudante = valor_total_combo * 0.10
    valor_total_combo -= desconto_estudante

# Aplica desconto fixo se valor final for maior que 200 ✅ 
if valor_total_combo > 200:
    valor_total_combo -= 15

# Exibe o valor final a pagar ✅ 
print("Valor final a pagar: R$ {:.2f}".format(valor_total_combo))
