def valida_senha(senha_inserida):
    qtd_caracteres_senha = len(senha_inserida)
    if qtd_caracteres_senha >= 6:
        return "Senha válida"
    else:
        return "Senha inválida, digite novamente uma senha de no mínimo 6 caracteres"


senha_inserida = input("Olá usuário, digite uma senha de no mínimo 6 caracteres para entrar no sistema: ")
print(valida_senha(senha_inserida))