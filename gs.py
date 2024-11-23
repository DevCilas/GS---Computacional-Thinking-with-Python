def so_numero(msg1, msg2):
    while True:
        num = input(msg1)
        try:
            num = float(num)
            return num
        except ValueError:
            print(msg2)

def media(lista_selecionada):

    ultimos_tres = lista_selecionada[-3:]
    soma = 0
    for num in ultimos_tres:
        soma += num
        media_num = soma/3
    return media_num

def so_cadastrados(lista_selecionada, msg1, msg2):
    element = input(msg1)
    while element not in lista_selecionada:
        element = input(msg2)
    return element


s_n = ['Sim', 'sim', 'Não', 'não']
contas = []
numero_creditos = 0

print("LIGHTSAVER: Defina metas, cumpra objetivos")

print("Vamos começar!")

print("Primeiro vamos calcular a média das suas últimas 3 contas:")
conta1 = so_numero("1ª Conta: R$", "Digite um valor válido: R$")
contas.append(conta1)

conta2 = so_numero("2ª Conta: R$", "Digite um valor válido: R$")
contas.append(conta2)

conta3 = so_numero("3ª Conta: R$", "Digite um valor válido: R$")
contas.append(conta3)


media_contas = media(contas)
media_atual = media_contas


reducao_15 = media_atual * 0.85
reducao_25 = media_atual * 0.75
reducao_30 = media_atual * 0.70

print(f"Sua média atual é R${media_contas:.2f}. Veja abaixo a tabela de créditos:")
print("REDUÇÃO   -   CRÉDITOS")
print("  15%     -      15C ")
print("  25%     -      25C ")
print("  30%     -      35C ")


continuar = so_cadastrados(s_n, "Deseja cadastrar outra conta? SIM ou NÃO\n-> ", "Digite uma opção válida\n-> ")

if continuar in ['Não', 'não']:
    print("Volte sempre!")
else:
    while True:
        nova_conta = so_numero("Nova Conta: R$", "Digite um valor válido: R$")
        contas.append(nova_conta)
        nova_media = media(contas)

        if nova_media <= reducao_30:
            print(f"Sua nova média é R${nova_media:.2f}. Parabéns! Você ganhou 35C.")
            numero_creditos += 35
            print("35 Créditos foram adiconados a sua conta!")
        elif nova_media <= reducao_25:
            print(f"Sua nova média é R${nova_media:.2f}. Parabéns! Você ganhou 25C.")
            numero_creditos += 25
            print("25 Créditos foram adiconados a sua conta!")
        elif nova_media <= reducao_15:
            print(f"Sua nova média é R${nova_media:.2f}. Parabéns! Você ganhou 15C.")
            numero_creditos += 15
            print("15 Créditos foram adiconados a sua conta!")
        else:
            print(f"Sua nova média é R${nova_media:.2f}. Não houve redução suficiente para ganhar créditos.")


        print(f"Total de créditos: {numero_creditos}")
        continuar = so_cadastrados(s_n, "Deseja cadastrar outra conta? SIM ou NÃO\n-> ", "Digite uma opção válida\n-> ")
        if continuar.lower() in ['não']:
            print(("Os créditos conquistados podem ser trocados por recompensas na nossa plataforma."))
            print("Obrigado por usar o LIGHTSAVER. Até a próxima!")
            break
