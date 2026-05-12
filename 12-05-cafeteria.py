"""Exiba um mini-menu: "Bem-vindo! O que deseja hoje? Temos 'cafe', 'cha' ou 'chocolate'."
Peça ao usuário para digitar sua escolha.
Se a escolha for "cafe", exiba: "Um café expresso saindo! Fica R$ 5,00."
Senão, se a escolha for "cha", exiba: "Ótima escolha! Seu chá de camomila fica R$ 6,00."
Senão, se a escolha for "chocolate", exiba: "Preparando seu chocolate quente cremoso! Fica R$ 8,00."
Caso contrário, exiba: "Desculpe, não temos essa opção no menu hoje."""

import os

cardapioValor = {"cafe": 5.50, "cha": 6.00, "chocolate": 8.00}
cardapio = {"cafe": "cafe", "cha": "cha", "chocolate": "chocolate"}
selection = 0
selection = int(
    input(f"""
    ---BEM VINDO! O QUE DESEJAS HOJE?-------
    ---1 - CAFÉ-------- R${cardapioValor["cafe"]}
    ---2 - CHA--------- R${cardapioValor["cha"]}
    ---3 - CHOCOLATE--- R${cardapioValor["chocolate"]}
    ---DIGITE O NÚMERO CORRESPONDENTE AO SEU PEDIDO:  """)
)
os.system("cls" if os.name == "nt" else "clear")
if selection > 3 or selection < 0:
    print("Número inválido, executar programa novamente")
elif selection == 1:
    print(f"Um café expresso saindo! Fica R$ {cardapioValor['cafe']}.")
elif selection == 2:
    print(f"Ótima escolha! Seu chá de camomila fica R$ {cardapioValor['cha']}")
elif selection == 3:
    print(
        f"Preparando seu chocolate quente cremoso! Fica R${cardapioValor['chocolate']}"
    )
