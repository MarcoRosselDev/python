notas = {
    'marco': 7,
    'marianella': 6,
    'eduardo': 5,
    'pepe': 7,
}
with open("frases.txt", "a") as file:
    for nombre, nota in notas.items():
        file.write(nombre + str(nota) + '\n')
import os
print("Directorio actual:", os.getcwd())