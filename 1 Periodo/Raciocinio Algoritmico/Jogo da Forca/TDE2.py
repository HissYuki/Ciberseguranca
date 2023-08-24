### TDE 2  da matéria de Raciocínio Algorítimico do curso de Cibersegurança - Jogo da Forca
### Aluno: Marco Aurelio Nissikawa Hisatomi

### Professor, não sei porque, mas já havia um código enviado na minha tarefa, porém eu fiz esse trabalho sozinho, e não estou conseguindo
### me desvincular do grupo da atividade formativa pelo AVA, então, por favor, considerar esse código e que apenas eu o implementei. Vou
### conversar com você sobre isso em sala também.

# Import das bibliotecas necessárias
import random
import pickle

def guess_verification(guess, used):
    for letter in used:
        if(letter == guess):
            print('Você já chutou essa letra. Por favor, tente novamente!')
            n_guess = input('Chute uma letra: ')
            return False, n_guess
    if(len(guess) != 1):
        print('Valor inválido. Por favor, tente novamente!')
        n_guess = input('Chute uma letra: ')
        return False, n_guess
    else:
        return True, guess
    

# Palavras pré-definidas para o jogo
easy = ['Mesa', 'Largo', 'Porta', 'Gato', 'Hoje', 'Texto']
medium = ['Canastra', 'Tratado', 'Ligamento', 'Abacaxi', 'Gafanhoto', 'Cadeado']
hard = ['Protagonista', 'Caixeiro viajante', 'Habilidade', 'Retificado', 'Atropelado', 'Tradicional']

# Guardando elas no arquivo
easy_doc = open('Easy.pkl', 'wb')
medium_doc = open('Medium.pkl', 'wb')
hard_doc = open('Hard.pkl', 'wb')

pickle.dump(easy, easy_doc)
pickle.dump(medium, medium_doc)
pickle.dump(hard, hard_doc)

easy_doc.close()
medium_doc.close()
hard_doc.close()

# Iniciando o jogo
print('Deseja jogar o Jogo da Forca?')

play = input(' 1-Sim\n 2-Não\n')
while(play != '1'):
    if play == '2':
        print('Até a próxima! Fechando o programa.')
        exit()
    else:
        print('Valor inválido! Por favor digite novamente.')
        play = input('Deseja jogar?\n 1-Sim\n 2-Não\n')

# Abrindo os arquivos .pkl com as palavras guardadas dentro
e_pkl = open('Easy.pkl', 'rb')
m_pkl = open('Medium.pkl', 'rb')
h_pkl = open('Hard.pkl', 'rb')

easy = pickle.load(e_pkl)
medium = pickle.load(m_pkl)
hard = pickle.load(h_pkl)

e_pkl.close()
m_pkl.close()
h_pkl.close()

# Loop do jogo
while True:
    # Seleção da dificuldade
    print('Selecione a dificuldade:')
    dif = input(' 1-Fácil\n 2-Médio\n 3-Difícil\n')
    while(dif != '1' and dif != '2' and dif != '3'):
        print('Valor inválido! Por favor, digite novamente.')
        dif = input(' 1-Fácil\n 2-Médio\n 3-Difícil')

    # Randomização da palavra
    ans_rand = random.randint(0, 5)
    
    if(dif == '1'):
        ans = easy[ans_rand]
    elif(dif == '2'):
        ans = medium[ans_rand]
    else:
        ans = hard[ans_rand]

    ans_length = len(ans)
    guess_chance = ans_length
    ans_letters = [letter for letter in ans]
    guess_letters = ["_" for letter in ans]
    for letter in ans_letters:
        if(letter == ' '):
            guess_letters[ans_letters.index(letter)] = letter
    used_letters = []

    print(f'A palavra tem {ans_length} letras!')

    # Loop para as chances do jogo
    while(guess_chance > 0):
        print(f'Você tem {guess_chance} chutes!')
        for char in guess_letters:
            print(char, end=' ')
        guess = input('\nChute uma letra: ')

        # Tratamento do chute
        valid_guess = False
        while(valid_guess == False):
            valid_guess, guess = guess_verification(guess, used_letters)

        # Comparando o chute com cada caracter da resposta
        i = 0
        while(i < ans_length):
            if(ans_letters[i].lower() == guess.lower()):
                print('Acertou a letra!\n')
                guess_letters[i] = ans_letters[i]
            i += 1
        
        used_letters.append(guess)
        
        # Verificando se a resposta já foi acertada
        if(guess_letters == ans_letters):
            break

        guess_chance -= 1   #Diminuindo o número de chances a cada chute

    # Print da palavra a cada chute
    for char in guess_letters:
        print(char, end=' ')

    # Comparação dos dois arrays, para verificar se o jogador venceu ou não
    if(guess_letters == ans_letters):
        print('\nParabéns, você acertou a palavra!')
    else:
        print('\nQue pena, você não acertou a palavra!')

    # Input para saber se o jogador deseja jogar novamente
    continue_game = input('Deseja jogar de novo?\n 1-Sim\n 2-Não\n')
    while(continue_game != '1'):
        if(continue_game == '2'):
            print('Obrigado por jogar!')
            exit()
        else:
            print('Valor inválido! Por favor, digite novamente: ')
            continue_game = input('Deseja jogar de novo?\n 1-Sim\n 2-Não\n')