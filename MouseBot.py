import win32api
import random
import time

# Developed by Angel de Jesús Manzo Rosas as BionicHawk
print ("Iniciando bot...")

# This function changes the cursor's position, giving it a random position
def cambiarPosicion ():
    x = 200 + int (random.random () * 600)
    y = 200 + int (random.random () * 500)
    print (f"Moviendo cursor a posición ({x}, {y})")
    win32api.SetCursorPos ( (x, y) )

# This function creates an infinite loop that calls the function "cambiarPosicion" every 60 seconds
def loopMouse ():
    while True:
        print ("Esperando a ejecutar instrucciones...")
        for x in  range (0, 60):
            print (f"Segundo: {x}")
            time.sleep (1)
        cambiarPosicion ()

# Calls the loop function
loopMouse ()


