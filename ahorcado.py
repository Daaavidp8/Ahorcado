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

    Categories = 'FRUTAS COCHES PAISES'.split()
    Fruits = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON ' \
             'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()
    Cars = "FORD TOYOTA MERCEDES AUDI BMW KIA VOLKSWAGEN DACIA SEAT PEUGOT NISSAN".split()
    Countries = "ESPAÑA ALEMANIA FRANCIA PERU ITALIA RUSIA ESLOVENIA ESLOVAQUIA SUIZA SUECIA ARGENTINA CANADA".split()

    def __init__(self, fname):
        self.name = fname
        self.categoria = random.choice(self.Categories)
        self.secreto = self.setcategoria(self.categoria)

    def jugar(self):
        secreto = self.secreto
        wrongletter = []
        correctletter = []

        while True:
            self.dibujar(wrongletter, correctletter, secreto)

            currentletter = self.dimeletra(wrongletter + correctletter, len(wrongletter))

            if currentletter in secreto:

                correctletter.append(currentletter)

                win = True
                for secretletter in secreto:
                    if secretletter not in correctletter:
                        win = False
                        break
                if win:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print(f'Has ganado, {self.name}!')
                    break
            else:
                wrongletter.append(currentletter)

                if len(wrongletter) == len(self.ESTADOS) - 1 or currentletter.lower() == "terminar":
                    if currentletter.lower() == "terminar":
                        print(self.ESTADOS[len(self.ESTADOS) - 1])
                        print("Programa Finalizado por el usuario")
                    else:
                        self.dibujar(wrongletter, correctletter, secreto)
                        print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    break

    def dibujar(self, letrasincorrectas, letrascorrectas, secreto):
        print(self.ESTADOS[len(letrasincorrectas)])
        print('La categoría es: ', self.categoria)
        print()

        print('Letras incorrectas: ', end='')
        for letter in letrasincorrectas:
            print(letter, end=' ')
        if len(letrasincorrectas) == 0 and 0 == len(letrasincorrectas):
            print('No hay letras incorrectas.')
        elif len(letrasincorrectas) == len(letrasincorrectas) + 1:
            print('Letras diferentes.')
        elif len(letrasincorrectas) == len(letrasincorrectas) + 2:
            print('No coinciden.')

        print()

        spa = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in letrascorrectas:
                spa[i] = secreto[i]

        print(' '.join(spa))

    def dimeletra(self, respuestas, numletrasincorrectas):
        while True:
            print('Adivina una letra.')
            self.intentosrestantes(numletrasincorrectas)
            adivina = input('> ').upper()
            if adivina.lower() == "terminar":
                return adivina
            elif len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in respuestas:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')

            else:
                return adivina

    def intentosrestantes(self, numletrasincorrectas):
        intentos = (len(self.ESTADOS) - 1) - numletrasincorrectas
        print(f"Tienes {intentos} intentos")

    def setcategoria(self, fcategoria):
        if fcategoria == "FRUTAS":
            return random.choice(self.Fruits)
        elif fcategoria == "COCHES":
            return random.choice(self.Cars)
        elif fcategoria == "PAISES":
            return random.choice(self.Countries)


if __name__ == '__main__':
    name = str(input("Dime tu nombre"))
    juego1 = JuegoAhorcado(name)
    juego1.jugar()
