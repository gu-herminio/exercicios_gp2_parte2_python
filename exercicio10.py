def checagem_autoricao_dirigir(cnh,idade):
    if cnh == "1" and idade >=18:
        situacao = "Apto para dirigir."
    else:
        situacao = "Não está apto para dirigir."
    
    return situacao


print("Informe seus dados para verificar sua autorização para dirigir: ")
idade = int(input("Digite sua idade:\n"))
cnh = input("Possui CNH?  1-Sim || 2-Não \n")
print(checagem_autoricao_dirigir(cnh,idade))