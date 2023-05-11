import random


class JuegoAhorcado:
    ESTADOS = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    SALVADO = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    Categories = 'FRUTAS'
    Words = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
            'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def jugar(self):

        wrongletter = []
        correctletter = []
        secreto = random.choice(self.Words)

        while True:
            self.dibujar(wrongletter, correctletter, secreto)

            currentletter = self.dimeletra(wrongletter + correctletter)

            if currentletter in secreto:

                correctletter.append(currentletter)

                win = True
                for secretletter in secreto:
                    print(correctletter)
                    print(secretletter)
                    if secretletter not in correctletter:
                        win = False
                        break
                if win:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado!')
                    break
            else:
                wrongletter.append(currentletter)

                if len(wrongletter) == len(self.ESTADOS) - 1:
                    self.dibujar(wrongletter, correctletter, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, letrasincorrectas, letrascorrectas, secreto):
        print(self.ESTADOS[len(letrasincorrectas)])
        print('La categoría es: ', self.Categories)
        print()

        print('Letras incorrectas: ', end='')
        for letter in letrasincorrectas:
            print(letter, end=' ')
        if len(letrasincorrectas) == 0 and 0 == len(letrasincorrectas):
            print('No hay letras incorrectas.')
        if len(letrasincorrectas) == len(letrasincorrectas) + 1:
            print('Letras diferentes.')
        if len(letrasincorrectas) == len(letrasincorrectas) + 2:
            print('No coinciden.')

        print()

        spa = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in letrascorrectas:
                spa[i] = secreto[i]

        print(' '.join(spa))

    def dimeletra(self, respuestas):
        while True:
            print('Adivina una letra.')
            adivina = input('> ').upper()
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in respuestas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina


if __name__ == '__main__':
    juego1 = JuegoAhorcado()
    juego1.jugar()
