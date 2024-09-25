while True:
    num1 = float(input('Digite o número: '))
    num2 = float(input('Digite outro número: '))
    print('-'*30)
    print('CALCULADORA'.center(30))
    print('-'*30)
    print('OPERAÇÕES'.center(30))
    print('~'*30)
    print('''1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão''')
    print('~'*30)
    while True:
        while True:
            try:
              op = int(input('Qual o código da operação que você deseja realizar? '))
              if not 1 <= op <= 4:
                print('Digite apenas opções válidas!')
              else:
                  break
            except (ValueError, TypeError):
                print('Digite um número válido!')

        if op == 1:
            print(f'O resultado da soma de {num1} e {num2} é {num1+num2}')
        elif op == 2:
            print(f'O resultado da subtração de {num1} por {num2} é {num1-num2}')
        elif op == 3:
            print(f'O resultado da multiplicação de {num1} por {num2} é {num1*num2}')
        else:
            print(f'O resultado da divisão de {num1} e {num2} é {num1/num2}')
        dnv = input('Deseja realizar outra operação com os mesmos números? [S/N]: ').strip()
        if dnv in 'Nn':
            break
    resp = input('Deseja realizar outra operação? [S/N]: \n').strip()
    if resp in 'Nn':
        break