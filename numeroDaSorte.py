import random
laco  = True
try:
    while laco:
        numAleatorio = random.randrange(0, 10)
        numeroDoUsuario = int(input('Digite um número entre 0 e 10: '))
        if numeroDoUsuario == numAleatorio:
            print('Você ganhou :)')
            break
        else:
            print('Você perdeu :(')
            continue
except:
    print('Algo deu errado :(')