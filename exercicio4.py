
def valida_numero(numero1,numero2):
    if numero1 > numero2:
        print(f"O número {numero1} é maior que {numero2}.")
    elif numero1 < numero2:
        print(f"O número {numero2} é maior que {numero1}.")
    else:
        print(f"Os números são iguais.")


print("Digite dois números abaixo para verificar qual é o maior: ")
numero1= float(input("Digite o primeiro número: "))
numero2= float(input("Digite o segundo número: "))
valida_numero(numero1,numero2)