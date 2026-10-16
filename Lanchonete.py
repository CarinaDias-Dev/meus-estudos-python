hamburguer = 10.50
batata_frita = 4.00
refrigerante = 3.00

quantidade_hamburguer = int(input("Informe a quantidade de hamburguer desejada: "))
quantidade_batata = int(input("Informe a quantidade de batata frita desejada: "))
quantidade_refrigerante = int(input("Informe a quantidade de refrigerante desejada:  "))

preco_total = (hamburguer*quantidade_hamburguer) + (batata_frita*quantidade_batata) + (refrigerante*quantidade_refrigerante)

print("=-"*20)
print("PREÇO TOTAL DO PEDIDO")
print("=-"*20)
print(f"O preço total do seu pedido foi R${preco_total:.2f}")
