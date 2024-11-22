def so_numero(msg1, msg2):
    num = input(msg1)
    while not num.isnumeric():
        num = input(msg2)
    num = int(num)
    return num


def media(lista_selecionada):
    i = len(lista_selecionada)
    soma = 0
    for num in range(1, 4):
        i -= num
        soma += lista_selecionada[i]
    media = soma / 3
    return media


print("LIGHTSAVER: Defina metas, cumpra objetivos ")

print("Vamos começar!")
contas = []
print("Primeiro vamos calcular a média das suas últimas 3 contas:")
conta1 = so_numero("1ª Conta: ", "Digite um valor válido: ")
contas.append(conta1)
conta2 = so_numero("2ª Conta: ", "Digite um valor válido: ")
contas.append(conta2)
conta3 = so_numero("3ª Conta: ", "Digite um valor válido: ")
contas.append(conta3)
conta4 = so_numero("4ª Conta: ", "Digite um valor válido: ")
contas.append(conta4)

media_contas = media(contas)

print(media_contas)



