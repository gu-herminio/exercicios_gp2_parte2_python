idade = int(input(f"Digite sua idade para confirmar se você está apto para votar: "))

if (idade >= 16):
    print(f"Sua idade é {idade}, você está apto para votar")
else:
    print(f"Sua idade é {idade}, ainda faltam {16-idade} anos para você estar apto para votar.")
