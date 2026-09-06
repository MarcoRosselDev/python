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
1:12:37