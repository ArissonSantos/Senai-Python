"""Defina quatro variáveis com notas de 0 a 10
Calcule a média das notas(somar todas as notas e dividir por 4)
Se a média for maior ou igual a 7, exibe: "Parabéns, você foi aprovado!"
Senão, se a nota for maior ou igual a 5(mas menor do que 7), exibe: "Você está de recuperação."
Caso contrário, deve exibir: "Que pena, você foi reprovado!"""

"""subject1 = int(input("Insira primeira nota: "))
subject2 = int(input("Insira primeira nota: "))
subject3 = int(input("Insira primeira nota: "))
subject4 = int(input("Insira primeira nota: "))

average = (subject1 + subject2 + subject3 + subject4) / 4

print(f"{average}")"""

grade = {"math": float(), "lang": float(), "phi": float(), "geo": float}

grade["math"] = float(input("Insira nota de matemática: ").replace(",", "."))
grade["lang"] = float(input("Insira nota de linguagens: ").replace(",", "."))
grade["phi"] = float(input("Insira nota de filosofia: ").replace(",", "."))
grade["geo"] = float(input("Insira nota de geografia: ").replace(",", "."))

average = float((grade["math"] + grade["lang"] + grade["phi"] + grade["geo"])) / 4

if average >= 7:
    print(f"sua média é {average}, você foi aprovado. Sucumba!")
elif average < 5:
    print(f"sua média é {average}, vc ta reprovado filhão, burro pa carai kkkkkkkk")
elif average > 5 and average < 7:
    print(
        f"sua média é {average}, vc ta de recuperação, ainda há esperanças para seu rabo patético"
    )
