def valida_nota(nota):
    match nota:
        case nota if nota >= 7:
            print(f"O aluno foi aprovado!")
        case nota if nota <7:
            print(f"O aluno foi reprovado!")
        
        case _:
            print("Insuficiente")

nota = int(input("Digite a nota para validar a situação do aluno: "))
valida_nota(nota)
        
