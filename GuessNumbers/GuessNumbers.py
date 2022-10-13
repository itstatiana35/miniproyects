import random



guessesTaken = 0
minNumber = 0
maxNumber = 20

print("Estoy pensando en un número entre el " + str(minNumber) + " al " + str(maxNumber) + ".")

numberCorrect = random.randint(minNumber, maxNumber)

while guessesTaken < 6:
    print("¿En qué número estoy pensando?")
    numberGuess = input()
    numberGuess = int(numberGuess)
    guessesTaken = guessesTaken + 1

    if numberCorrect > numberGuess:
        print("El número es más grande.")

    if numberCorrect < numberGuess:
        print("El número es más pequeño.")

    if numberCorrect == numberGuess:
        break
   
if numberGuess == numberCorrect:
    print("Enorahuena, has acertado en " + str(guessesTaken) + " intentos.")   

if numberGuess != numberCorrect:
    print("Te has equivocado. El número que estaba pensando es " + str(numberCorrect) + ".")  
