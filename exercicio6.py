

def calculo_desconto(valor_compra):
    valor_desconto = (valor_compra *0.10)
    return valor_desconto



def valida_desconto(valor_compra):
    if valor_compra > 100.00:
        valor_atualizado = valor_compra - calculo_desconto(valor_compra)
    else:
        valor_atualizado = valor_compra

    return valor_atualizado


valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100.00:
    print(
        f"Valor da compra: R${valor_compra:.2f}\n"
        f"Valor do desconto de 10%: R${calculo_desconto(valor_compra):.2f}\n"
        f"Valor da compra atualizado com desconto de 10%: R${valida_desconto(valor_compra):.2f}"
    )

else:
        print(f"Valor da compra: {valor_compra} ")
