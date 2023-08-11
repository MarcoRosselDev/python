## 1. Declare your age as integer variable----------------------------------
my_age = 30

## 2. Declare your height as a float variable-------------------------------
my_hight = 1.72 # meters

## 3. Declare a variable that store a complex number------------------------
my_complex_number = 4j

## 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).-------
base = int(input('Enter the base of a triangle please : '))
hight = int(input('Enter the hight of a triangle please : '))

# formula es ( base x altura ) / 2
area_triangulo = base * hight * 0.5
print('El area del triangulo es = ', area_triangulo)

## 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).--------------------------------------------------------------------------

side_a = int(input('Enter side a of the triangle please : '))
side_b = int(input('Enter side b of the triangle please : '))
side_c = int(input('Enter side c of the triangle please : '))

perimetro_triangulo = side_a + side_b + side_c
print('El perimetro del triangulo es : ', perimetro_triangulo)

## 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))-----
length_rectangle = int(input('Plese enter the lenght of a rectangle : '))
width_rectangle = int(input('Plese enter the width of a rectangle : '))

area_rectangle = length_rectangle * width_rectangle
perimetro_rectangulo = ( length_rectangle + width_rectangle ) * 2

print('El area del rectangulo es : ', area_rectangle)
print('El perimetro del rectangulo es : ', perimetro_rectangulo)

## 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius_input = int(input('Enter a radius please : '))
area_circulo = ( radius_input ** 2 ) * pi
print('El area del circulo es : ', area_circulo)
perimetro_circunferencia = radius_input * 2 * pi
print('El perimetro del circulo es : ', perimetro_circunferencia)