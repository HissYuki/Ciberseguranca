# TDE 1 da matéria de Raciocínio Algotítmico
# Marco Aurelio Nissikawa Hisatomi

import random
import time

# Seleção de número de jogadores
print('Número de jogadores: \n 1 - Um jogador \n 2 - Dois jogadores')
n_jogadores = input('Selecione o número de jogadores: ')

# Seleção da dificuldade
print('Dificuldade: \n1 - Fácil \n2 - Médio \n3 - Difícil')
dif = input('Selecione a dificuldade: ')

# Singleplayer
if n_jogadores == '1':
    print('Resolva as 4 equações que serão apresentadas em 20 segundos cada(Aproxime a divisão para um número redondo): ')
    pont = 0                                    # Inicialização da pontuação em zero

    # Dificuldade fácil
    if dif == '1':
        # Primeira questão(Soma)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-10, 10)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

    # Dificuldade Média
    if dif == '2':
        # Primeira questão(Soma)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-100, 100)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

    # Dificuldade Difícil
    if dif == '3':
        # Primeira questão(Soma)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-1000, 1000)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

    print(f'A sua pontuação final é {pont}')

# Dois jogadores
elif n_jogadores == '2':
    pont = 0

    print('Jogador 1, resolva as 4 equações que serão apresentadas em 20 segundos(Aproxime a divisão para um número redondo):')

    # Dificuldade fácil
    if dif == '1':
        # Jogador 1
        # Primeira questão(Soma)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-10, 10)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont1 = pont
        pont = 0

        # Jogador 2
        print('Jogador 2, resolva as 4 equações que serão apresentadas em 20 segundos:')
        # Primeira questão(Soma)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-10, 10)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-10, 10)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-10, 10)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont2 = pont

    elif dif == '2':
        # Jogador 1
        # Primeira questão(Soma)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-100, 100)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont1 = pont
        pont = 0

        # Jogador 2
        print('Jogador 2, resolva as 4 equações que serão apresentadas em 20 segundos:')
        # Primeira questão(Soma)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-100, 100)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-100, 100)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-100, 100)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont2 = pont

    elif dif == '3':
        # Jogador 1
        # Primeira questão(Soma)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-1000, 1000)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont1 = pont
        pont = 0

        # Jogador 2
        print('Jogador 2, resolva as 4 equações que serão apresentadas em 20 segundos:')
       # Primeira questão(Soma)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 1
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 1
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} + ({num2}) = '))
        else:
            res = int(input(f'{num1} + {num2} = '))
        per = num1 + num2

        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Segunda questão(Subtração)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 2
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 2
        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} - ({num2}) = '))
        else:
            res = int(input(f'{num1} - {num2} = '))
        per = num1 - num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Terceira questão(Multiplicação)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 3
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 3

        time_init = time.time()

        if abs(num2) != num2:
            res = int(input(f'{num1} * ({num2}) = '))
        else:
            res = int(input(f'{num1} * {num2} = '))
        per = num1 * num2
        
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)

        # Quarta questão(Divisão)
        num1 = random.randint(-1000, 1000)          # Randomização do primeiro número da questão 4
        num2 = random.randint(-1000, 1000)          # Randomização do segundo número da questão 4

        time_init = time.time()

        while num2 == 0:                        # Verificação do segundo número da divisão, caso ele seja zero
            num2 = random.randint(-1000, 1000)
        if abs(num2) != num2:
            res = int(input(f'{num1} / ({num2}) = '))
        else:
            res = int(input(f'{num1} / {num2} = '))
        per = num1 // num2
        time_end = time.time()

        timer = time_end - time_init            # Calcula o tempo que levou para resolver a questão
        if timer >= 20:                          # Verifica se o tempo limite foi ultrapassado
            print('Você ultrapassou o limite de 20 segundos, a questão foi zerada!')
        elif res == per:                        # Incrementa a pontuação
            pont = pont + 10 * ((20 - int(timer)) * 0.05)
        
        pont2 = pont

    if pont1 >= pont2:
        print(f'Ranking:\n  Jogador 1: {pont1} \n  Jogador 2: {pont2}')
    else:
        print(f'Ranking:\n  Jogador 2: {pont2} \n   Jogador 1: {pont1}')

else:
    print('Entrada inválida!')