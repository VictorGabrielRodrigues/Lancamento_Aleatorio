import random
import time

print("#---------------Simulador de Cara ou Coroa---------------#\n")

escolha = input("Escolha entre Cara ou Coroa: ")
resultado = random.choice(["Cara","Coroa"])
print("#---------------Lançando a Moeda---------------#")
time.sleep(1)
if escolha==resultado:
    print("\n#----------O Resultado foi: ", resultado,"----------#")
    time.sleep(1)
    print("\nVocê Ganhou!!!!!")
else:
    print("\n#----------O Resultado foi: ", resultado,"----------#")
    time.sleep(1)
    print("\nVocê Perdeu!")