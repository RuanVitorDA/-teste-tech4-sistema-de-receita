print("##########################")
print("##Cadastro de medicamentos##")
print("############################")
nome = input("Digite o nome do paciente")


medicamentos = []
frequencias = []

repetir = ""

while repetir!= "fim":
    NomeMed = input("Digite o Nome do medicamento")
    medicamentos.append(NomeMed)

    print("medicamentos")
    dosgem = input("Dosagem do medicamento")
    frequencia.append(nomeMed)

    print("1. Adicionar Medicamento")
    print("2. Finalizar receita")

    opcao = int(input("Escolha a opção:"))
    if opcao == 1:
        repetir = ""
    if opcao ==2:
        repetir = "fim"

    print(medicamentos)
    print(frequencias)

for i in range(len(medicamentos)):
    print("medicamentos" , medicamentos[i] , "Frequencia", dosagem[i])
