# variables
sintaxis:
> \<nombre> = \<valor>

ejemplo:
```python
my_number = 5
```

# tipos de datos

## integer (enteros)

```python
type(-15) # <class 'int'>
type(0) # <class 'int'>
type(5) # <class 'int'>
```

## float (decimal o coma flotante)

```python
type(0.0) # <class 'float'>
type(-0.7) # <class 'float'>
type(100.0) # <class 'float'>
```

## boolean (boleanos)

```python
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>
```

## String (Cadena de caracteres)

```python
print(type("Python")) # <class 'str'>
```
### built-in fn----> len()
```python
print(len(55)) # object of type 'int' has no len()
print(len("python")) # 6
```

### slicing o revanada
sintaxis  
\<cadena>[inicio:fin]
```python
revanada = "python"[1:4]
print(revanada) # yth
```
Entonces el indice 4 de fin, no lo incluye, pero el indice inicio si se incluye.

```python
"como hacer saltos"[3:14:2] # ohcrsl
# 3=inicio:14=fin:2=salto ===> ohcrsl
```

## metodos de strings

\<cadena>.capitalize()
```python
"marco".capitalize() #= Marco
```
lista de metodos importantes:  
  * find   
  * index
  * isalnum
  * isalpha
  * isdecimal
  * isdigit
  * islower
  * isupper
  * lower
  * upper

### buitd-in fn---> input()
```python
num = input("Ingrese un número: ")
print(num)
```
al ingresar un numero, este regresa como string, por lo que se debe aplicar   
la funcion built-in---> int()
```python
num=int(input("Ingresa un numero: "))
```
En el caso de que quieras ingresar un boleano es un poco mas complejo
por ejemplo si en tu input ingresas algo asi:
```python
value = input("ingresa True o False")
```
El resultado sera un string no un valor booleano,   
para eso requeriras realizar una conversion y una validacion,   
algo asi:
```python
# Convierte el texto a minúsculas y elimina espacios innecesarios
val_str = input("Ingrese True o False: ").strip().lower()

# Retorna True solo si el usuario escribió "true", de lo contrario False
val_bool = val_str == "true"

print(type(val_bool))  # <class 'bool'>
print(val_bool)
```

# Operadores
diccionario:   
operador=Simbolos que denotan una opearacion   
operandos=Valores con los cuales se ejecuta la operacion.   
expresion=Combinacion de valores, variables y operadores que al ser evaluados resultan en un valor.   

> Operador + Operandos = Expresion

Operadores:
  1. Aritmeticos
  2. Logicos
  3. De Asignacion
  4. Relacionales

### Operadores Aritmeticos
Nos permiten realizar operaciones aritmeticas en el programa.
* suma +
* resta -
* multiplicacion *
* division /
* division entera //
* exponente **
* modulo %
### Operadores Logicos
Nos permiten trabajar con valores booleanos
* and
* or
* not

#### and
Tabla de verdad de and

| x  | y  | x and y |
|----|----|---------|
|True|True|True |
|True|False|False|
|False|True|False |
|False|False|False |
#### or
Tabla de verdad de or

| x  | y  | x or y |
|----|----|---------|
|True|True|True |
|True|False|True|
|False|True|True |
|False|False|False |
#### not
Tabla de verdad de not

| x  | not x  |
|----|----|
|True|False |
|False|True|

#### prioridad
* not  mayor prioridad "se evalua primero"
* and
* or  menor prioridad
Si existen varios operadores logicos de la misma prioridad se evaluan de izquierda a derecha.

### Operadores Relacionales
Son utilizados para comparar valores y retornan un valor booleano.
* \> mayor que
* \< menor que
* == igual que
* \>= mayor o igual
* \<= menor o igual
* \!= no igual que

### Operadores de asignacion
Son utilizados para asignar valores a las variables del programa.

* =
* -=
* /=
* //=
* +=
* *=
* **=
* %=

# Sentencias condicionales
```python
if <condicion>:   
    # codigo
elif <condicion2>:
    # codigo
else:
    # codigo
```
ejemplo:
```python
if value < 0:
    print("tu numero es negativo")
elif value == 0:
    print("tu numero es cero")
else:
    print("tu numero es positivo")
```

# Listas
Estructura de datos utilizada para almacenar multiples valores en secuencia.  

1. agregar un elemento al final de una lista   
\<lista>.append(\<elemento>)

2. agregar un elemento en un indice especifico  
\<lista>.insert(\<indice>, \<elemento>)

3. eliminar el primer elemento encontrado  
aplicar una verificacoin previa, por que si no, lanzara un error  
>\<element> in \<lista>  

then
>\<lista>.remove(\<elemento>)

4. saber el indice de la primera ocurrencia  
si no se encuentra ocurre un error, por lo que se debe verificar tambien.  
\<lista>.index(\<element>)

5. actualizar un valor en la lista  
\<lista>[\<indice>] = \<nuevo_valor>

## Metodos de las listas

* .count(elemento) cuenta las ocurrencias de un elemento en la lista
* .extend(lista) extiende una lista agregandole otra lista
* .pop() eliminia y retorna el ultimo elemento
* .reverse() invierte el orden de la lista
* .sort() ordena los elementos de la lista

# Tupla
Estructura de datos inmutable que contiene una secuencia ordenada de elementos.  

sintaxis:  
('a', 'b', 'c')

## Metodos de tuplas
* tupla.index(elemento) ---> para saber el indice de un elemento
* elemento in tupla ---> para saber si un elemento existe en la tupla
* tupla.count(elemento)

La principal diferencia entre las listas y tuplas es que las tuplas son inmutables, ideales para protejer los datos.

# Diccionarios
sintaxis:
```python
edades = {'gino': 35, 'nora': 45}
# dos formas de acceder a sus valores
#print(edades['gino']) # 35
#print(edades.get("gino")) # 35
```
remover:
```python
del diccionario[clave]
```
revisar existencia
```python
elemento in diccionario
```
# Ciclo for

sintaxis:
```python
for variable in range(inicio, fin):
    #codigo
```
ejemplo:
```python
cuantity = 5

for numero in range(1, cuantity + 1):
    print(numero)

""" output: 
1
2
3
4
5
 """
 # inicio = 1 porque si se omite, por defecto es 0 (inicio=0)
 
 # fin = cantidad + 1, porque por defecto no se incluye el digito final
```

El ciclo for itera sobre iterables, como:
* Cadena de caracteres
* Listas
* Tuplas
* Diccionarios
* funcion range()

ejemplo de un iterable strign
```python
for caracter in 'string':
    print(caracter)

# s
# t
# r
# i
# n
# g
```
## iterar por diccionarios
#### ITERAR POR CLAVES
podemos iterar por las claves, valores o pares clave-valor  
en el caso de las claves se puede pasar directamente el diccionario:

```python
my_dicc = {'name': 'marco', 'age': 33, 'pareja': True}

for clave in my_dicc:
    print(clave)
# name
# age
# pareja
```

#### ITERAR POR VALORES
pare iterar por los valores aplicamos .values() :
```python
my_dicc = {'name': 'marco', 'age': 33, 'pareja': True}

for clave in my_dicc.values():
    print(clave)
# marco
# 33
# True
```
#### ITERAR POR PAR CLAVE-VALOR
```python
my_dicc = {'name': 'marco', 'age': 33, 'pareja': True}

for clave, valor in my_dicc.items():
    print(clave, valor)
# name marco
# age 33
# pareja True
```
# Ciclo while
2:55:31