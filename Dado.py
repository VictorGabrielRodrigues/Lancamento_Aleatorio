import random
import time

print("#---------------Simulador de Dado---------------#\n")

dado = int(input("Escolha o numero de faces do Dado: "))
resultado = random.randint(1,dado)
print("#---------------Rolando o Dado---------------#")
time.sleep(1)
print("#---------------Resultado foi---------------#")
time.sleep(0.5)
print("#--------------------",resultado,"--------------------#")