def valida_faixa_etaria(idade):
    match idade:
        case idade if idade <=12:
            faixa_etaria = "Criança"
        case idade if idade >= 13 | idade <= 17:
            faixa_etaria = "Adolescente"
        case idade if idade >=18:
            faixa_etaria = "Adulto"

    return faixa_etaria


idade = int(input("Digite a sua idade para descobrir sua faixa etária: "))
print(f"A sua idade é {idade} portanto sua faixa etária é: {valida_faixa_etaria(idade)}")