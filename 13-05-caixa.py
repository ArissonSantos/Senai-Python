"""Defina uma variável com o saldo disponível
Pergunte ao usuário qual o valor da compra que ele deseja fazer
Caso não saiba como "Perguntar ao usuário", defina uma variável com o valor da compra.
Se o valor da compra for menor ou igual ao saldo, o programa deve exibir: "Compra aprovada! Obrigado."
Caso contrário, deve exibir: "Saldo insuficiente, compra negada!"""

import os
import time

balance = float(input("Quanta grana vc tem?"))
if balance < 1518.00:
    print("Coitadinho ta pobre kkkkkk")
    time.sleep(1.0)
    os.system("cls" if os.name == "nt" else "clear")


valCompra = float(input("Insira valor da compra: "))
if valCompra > balance:
    print("Você ta pobre demais pra isso meu filho")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
elif valCompra <= balance:
    print("Compra aprovada, bom proveito")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
