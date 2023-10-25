# Definição das funções

def dimensoesObjeto():  # Definição de função para receber e calcular as dimensões para retornar um valor multiplicador

    while True:  # Loop para garantir que o usuário digitará corretamente

        try:  # Tratamento para se o usuário digitar corretamente

            comprimento = int(input('Digite o comprimento do objeto (em cm): '))
            largura = int(input('Digite a largura do objeto (em cm): '))
            altura = int(input('Digite a altura do objeto (em cm): '))  # Leitura dos valores para calcular a dimensão

            dimensao = comprimento * largura * altura  # Calculo das medidas recebidas, que, resulta na dimensão

            print(f'O volume do objeto é (em cm³) {dimensao:.1f}')  # Informa ao usuário a dimensão do objeto

            if dimensao < 1000:  # Verifica o volume da dimensão
                return 10.00  # Retorna o valor para aquela dimensão

            elif dimensao < 10000:
                return 20.00

            elif dimensao < 30000:
                return 30.00

            elif dimensao < 100000:
                return 50.00

            else:  # Caso o valor seja maior do que o permitido informa ao usuário que não é aceito
                print('Não aceitamos objetos com dimensões tão grandes')

        except:  # Tratamento de erro para que se o usuário não digite um número inteiro

            print('Você digitou uma dimensão do objeto com valor não numérico')
            print('Por favor entre com as dimensões desejadas novamente')


def pesoObjeto():  # Definição de função para receber o peso e retornar um multiplicador

    while True:

        try:

            peso = float(input('Digite o peso do objeto (em kg): '))

            if peso < 0.1:
                return 1

            elif peso < 1:
                return 1.5

            elif peso < 10:
                return 2

            elif peso < 30:
                return 3

            else:
                print('Não aceitamos objetos tão pesados')

        except:
            print('Você digitou o peso do objeto com valor não numérico')

def rotaObjeto():  # Definição de função para receber verificar a rota e retornar um multiplicador

    while True:

        print('Selecione a rota:')
        print('''
        BR - De Brasília para Rio de Janeiro
        BS - De Brasília para São Paulo
        RB - De Rio de Janeiro para Brasília
        RS - De Rio de Janeiro para São Paulo
        SR - De São Paulo para Rio de Janeiro
        SB - De São Paulo para Brasília''')

        rota = input('>> ').upper()

        if rota == 'RS' or rota == 'SR':
            return 1

        elif rota == 'BS' or rota == 'SB':
            return 1.2

        elif rota == 'BR' or rota == 'RB':
            return 1.5

        else:
            print('Você digitou uma rota que não existe')

# Programa principal

print("Bem Vindo a Companhia de Logística Guilherme Araújo de Barros S.A. (RU: 4390675)")

multiplicadorDimensao = dimensoesObjeto()  # Chama a função e atribui seu retorno a variável
multiplicadorPeso = pesoObjeto()
multiplicadorRota = rotaObjeto()

total = multiplicadorDimensao * multiplicadorPeso * multiplicadorRota  # Calcula os multiplicadores recebidos

print(f'Total a pagar (R$): {total:.2f} (dimensões: {multiplicadorDimensao:.1f} * peso: {multiplicadorPeso:.1f} * rota: {multiplicadorRota:.1f})')
# Imprime o total a pagar e informa como foi feito o calculo
