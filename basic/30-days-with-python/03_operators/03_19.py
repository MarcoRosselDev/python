## 19. Check if type of '10' is equal to type of 10

type_of_value = 10 == '10'
print(type_of_value) # False

## 20. Check if int('9.8') is equal to 10
# ninety_eight = int('9.8')
# print(ninety_eight) # False, not iqual to 10

## 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours_worked = int(input('Cuantas horas trabajaste? : '))
precio_por_hora = int(input('Cuanto te pagan la hora de trabajo? : '))

dinero_ganado = hours_worked * precio_por_hora
print('ganaste = ', dinero_ganado)