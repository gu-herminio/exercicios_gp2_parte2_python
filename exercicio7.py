def retorna_dia_semana(numero):
    match numero:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-feira")
        case 3:
            print("Terça-feira")
        case 4:
            print("Quarta-feira")
        case 5:
            print("Quinta-feira")
        case 6:
            print("Sexta-feira")
        case 7:
            print("Sábado")
        case _:
            print("Inválido")


numero = int(input("Digite um número: "))
retorna_dia_semana(numero)