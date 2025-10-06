def calcula_classificacao(nota):
    if nota >= 90 and nota <=100:
        classificacao = "A"
    elif nota >= 80 and nota <=89:
        classificacao = "B"
    elif nota >= 70 and nota <=79:
        classificacao = "C"   
    elif nota >= 60 and nota <=69:
        classificacao = "D"
    elif nota <=59:
        classificacao = "F"
    else:
        classificacao = "Inválido"

    return classificacao


nota = int(input("Digite a nota do aluno: "))
print(f"A classificação do aluno é: {calcula_classificacao(nota)}")

        
