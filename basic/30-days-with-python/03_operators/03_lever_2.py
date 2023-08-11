## 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 0
y = 2*x - 2
print('Interseccion en eje y cuando x es cero es : ', y) ## -2
y = 0
x = (y/2) + 1
print('Interseccion en eje x cuando y es cero es: ', x) ## 1

## 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance] between point (2, 2) and point (6,10)

x1 = int(input('Enter the x1 value please : '))
y1 = int(input('Enter the y1 value please : '))
x2 = int(input('Enter the x2 value please : '))
y2 = int(input('Enter the y2 value please : '))

pendiente = (y2 - y1)/(x2 - x1) # 2
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2) # 8.9442719099
print('La pendiente de estos dos puntos son : ', pendiente)
print('La distancia euclideana entre estos dos punto es : ', euclidean_distance)

## 10. Compare the slopes in tasks 8 and 9.---------------------------------
# la pendiente de el ejercicio 8 es 2
# la pendiente del ejecicio 9 es 2  ---> tienen la misma pendiente