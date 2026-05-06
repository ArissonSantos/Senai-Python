import os
User = {
    "Name" : "None",
    "Age" : 0,
    "Role" : "None"
}
User["Name"] = input("Digite seu nome: ")
User["Age"] = input("Insira sua idade: ")
User["Role"] = input("Insira sua função: ")
os.system("cls" if os.name == "nt" else "clear")
print(f"""Name: {User["Name"]}
Age: {User["Age"]}
Role: {User["Role"]}""")