listaPecas = []  # Lista criada para receber o dicionário com as peças
codigo = 0  # Cria o código exclusivo

# Definição das funções
def cadastrarPeca(codigo):  # Definição de função para cadastrar uma nova peça
    peca = {}
    print('Você selecionou a Opção de Cadastrar Peça')

    while True:  # Cria um loop que será usado para garantir que usuário no campo "VALOR" digite um número
        try:
            print(f'Código da peça {codigo:03d}')  # Informa o código exclusivo da peça
            peca['codigo'] = codigo  # Armazena o código dentro do dicionário onde a peça estará
            peca['nome'] = input('Por favor entre com o NOME da peça: ').upper()  # Pede para que o usuário informe os dados da peça
            peca['fabricante'] = input('Por favor entre com o FABRICANTE da peça: ').upper()
            peca['valor'] = float(input('Por favor entre com o VALOR da peça: '))
            listaPecas.append(peca)  # Armazena os dados dentro de uma lista
            break  # Para o loop

        except:  # Caso o usuário não digite um valor imprime a mensagem abaixo
            print('Favor digitar no campo "VALOR" um valor numérico')
            continue  # Volta para o início do loop


def consultarPeca():  # Definição de função para consultar peça
    print('Você selecionou a Opção de Consultar Peças')
    while True:

        print('Escolha a opção desejada: \n1-Consultar Todas as Peças \n2-Consultar Peças por Código \n3-Consultar peças por Fabricante \n4-Retornar')
        opcaoConsulta = input('>> ')  # Pede que o usuário digite a opção desejada

        if opcaoConsulta == '1':  # Analisa a opção escolhida e mostra os dados desejados (peça por peça)
            print('-' * 24)
            
            for peca in listaPecas:
                print(f'Código: {peca["codigo"]} \nNome: {peca["nome"]} \nFabricante: {peca["fabricante"]} \nValor: {peca["valor"]:.2f}')
                print('-' * 24)
                continue

        elif opcaoConsulta == '2':
            consultaCodigo = input('Digite o CÓDIGO da Peça: ')  # Pede que o usuário digite o parâmetro da peça
            encontrado = False
            
            for peca in listaPecas:
                if str(peca['codigo']) == consultaCodigo:  # Analisa o parâmetro das peças e imprime a compatível
                    print('-' * 24)
                    print(f'Código: {peca["codigo"]} \nNome: {peca["nome"]} \nFabricante: {peca["fabricante"]} \nValor: {peca["valor"]:.2f}')
                    print('-' * 24)
                    encontrado = True
                    continue

            if not encontrado:  # Caso não encontre o código imprime a mensagem abaixo e volta ao início do loop
                print('')
                print('Código não encontrado')
                print('')
                continue

        elif opcaoConsulta == '3':
            consultaFabricante = input('Digite o FABRICANTE da Peça: ').upper()
            print('-' * 34)
            encontrado = False

            for peca in listaPecas:
                if str(peca['fabricante']) == consultaFabricante:
                    print(f'Código: {peca["codigo"]} \nNome: {peca["nome"]} \nFabricante: {peca["fabricante"]} \nValor: {peca["valor"]:.2f}')
                    print('-' * 34)
                    encontrado = True
                    continue

            if not encontrado:
                print('')
                print('Fabricante não encontrado')
                print('')
                continue

        elif opcaoConsulta == '4':
            break

        else:  # Caso não tenha digitado alguma das alternativas acima imprime a mensagem abaixo e volta ao início do loop
            print('Opção Inválida')
            continue


def removerPeca():  # Definição de função para remover peça
    print('Você Selecionou a Opção de Remover Peça')
    pecaRemove = input('Digite o código da peça a ser removida: ')  # Pede que digite o código da peça a ser removida
    encontrado = False

    for peca in listaPecas:  # Verifica as peças

        if pecaRemove == str(peca['codigo']):  # Verifica se a peça existe
            listaPecas.remove(peca)  # Remove a peça da lista
            encontrado = True
            print('Peça removida')
            print('')
            
    if not encontrado:  # Verifica se a peça não foi encontrada e mostra a mensagem abaixo
        print('')
        print('Peça não encontrada')
        print('')


# Programa principal

print('Bem Vindo ao Controle de Estoque da Bicicletaria do Guilherme Araújo de Barros (RU: 4390675)')

while True:

    print('Escolha a opção desejada: \n1-Cadastrar Peças \n2-Consultar Peças \n3-Remover Peças \n4-Sair')
    escolhaOpcao = input('>> ')  # É apresentado as opções acima e pede para selecionar uma delas

    if escolhaOpcao == '1':  # Analisa a opção selecionada
        codigo = codigo + 1  # Atualiza o código exclusivo
        print('')
        cadastrarPeca(codigo)  # Chama a função e a executa
        print('')
        continue  # Volta para o início do loop

    elif escolhaOpcao == '2':
        print('')
        consultarPeca()
        print('')
        continue

    elif escolhaOpcao == '3':
        print('')
        removerPeca()
        print('')
        continue

    elif escolhaOpcao == "4":  # Analisa a opção sair e finaliza o programa no break
        break

    else:
        print('Opção Inválida')  # Tratamento caso o usuário não digite uma opção válida e volta ao início do loop
        print('')
        continue
