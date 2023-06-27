# Raciocínio Algorítmico . TDE 3 - Jogo da Memória
# Primeiro Período do curso de Cibersegurança da PUCPR
# Autores: Alexandre Mendes Taborda, Henrique Muller Papai, João Henrique Ferreira Kruger, Marco Aurelio Nissikawa Hisatomi

import random
import time
import os


def main():
  os.system('clear')
  mat, mat_exib, run_game, cont_x = setup()

  #Loop do jogo
  while (run_game):
    #Print das peças no console
    print(' ', end='  ')
    for i in range(len(mat_exib)):
      print(i + 1, end='  ')
    print('')
    for l in range(len(mat_exib)):
      print(l + 1, end='  ')
      for c in range(len(mat_exib)):
        print(mat_exib[l][c], end='  ')
      print('\n')

    choice = int(
      input(
        'Você deseja tentar adivinhar, xeretar as respostas ou desistir? \n\n1 - Tentar adivinhar \n2 - Xeretar\n3 - Desistir\n'
      ))
    if choice == 1:
      pos1 = [
        int(input('Digite uma linha: ')) - 1,
        int(input('Digite uma coluna: ')) - 1
      ]
      pos2 = [
        int(input('Digite uma linha: ')) - 1,
        int(input('Digite uma coluna: ')) - 1
      ]
      print(pos1, pos2)
      mat, mat_exib = atualiza(pos1, pos2, mat, mat_exib)
    elif choice == 2:
      if cont_x < 2:
        exibir_resp(mat)
        cont_x += 1
      else:
        print('Você já gastou as suas xeretadas')
    elif choice == 3:
      desistencia()

    run_game = checa_fim_de_jogo(mat, mat_exib)

    if run_game == False:
      res = int(
        input('Você deseja recomeçar ou sair? \n\n1 - Recomeçar \n2 - Sair\n'))
      if res == 1:
        mat, mat_exib, run_game, cont_x = setup()
  print('Até a próxima!')


#Inicializa todas as variáveis necessárias para o jogo começar
def setup():
  menu = int(input('Escolha a dificuldade: \n1-Fácil \n2-Médio \n3-Díficil\n'))
  mat, mat_exib = criar_matriz(menu)
  run_game = True
  cont_x = 0
  return mat, mat_exib, run_game, cont_x


#Cria a matriz com os pares espalhados aleatoriamente e a matriz de exibição do jogo com '#'
def criar_matriz(dif):
  mat = []
  mat_exib = []
  used = []
  letras = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
    "e", "f"
  ]
  dim = (dif + 1) * 2
  r = (dim**2) // 2

  for i in range(r):
    used.append(0)
  for l in range(dim):
    mat.append([])
    mat_exib.append([])
    for c in range(dim):
      rand = random.randint(0, r - 1)

      while (used[rand] == 2):
        rand = random.randint(0, r - 1)
      mat[l].append(letras[rand])
      used[rand] += 1
      mat_exib[l].append('#')

  return mat, mat_exib


#Verifica se o chute foi correto e atualiza a matriz de exibição
def atualiza(pos1, pos2, mat, mat_exib):

  if mat[pos1[0]][pos1[1]] == mat[pos2[0]][pos2[1]]:
    mat_exib[pos1[0]][pos1[1]] = mat[pos1[0]][pos1[1]]
    mat_exib[pos2[0]][pos2[1]] = mat[pos2[0]][pos2[1]]
    os.system('clear')
    print('Parabens, você acertou')
  else:
    os.system('clear')
    print('Que pena, você errou!')

  return mat, mat_exib


#Exibe a resposta do jogo na tela por 5 segundos
def exibir_resp(mat):
  for l in range(len(mat)):
    for c in range(len(mat)):
      print(mat[l][c], end='    ')
    print('')
  time.sleep(5)
  os.system('clear')


#Verifica se o jogo deve terminar
def checa_fim_de_jogo(mat, mat_exib):
  if mat == mat_exib:
    return False
  return True


#Fecha o jogo em caso de desistência
def desistencia():
  os.system('clear')
  exit('Até a próxima!')


if __name__ == '__main__':
  main()
