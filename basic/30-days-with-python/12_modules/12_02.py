""" 2. Modify the previous task. Declare a function named user_id_gen_by_user. 
It doesn’t take any parameters but it takes two inputs using input(). 
One of the inputs is the number of characters and the second input is the number 
of IDs which are supposed to be generated. """

""" output example:
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr """

from random import randint

letters_min_list =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers_list =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters_may_list =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def random_user_id(lenght, repetitions):
    def random_one():
        id = ''                                                                             # string donde agregar los valores en cada iteracion
        for iteration in range(0, lenght):
            random_type_list = randint(0, 2)
            if random_type_list == 0:                                                       # si es 0 iteramos aleatoriamente por la lista de letras minusculas
                random_letters_list_index = randint(0, len(letters_min_list) - 1 )
                id = id + letters_min_list[random_letters_list_index]
            elif random_type_list == 1:                                                     # si es 1 iteramos aleatoriamente por la lista de numeros
                random_numbers_list_index = randint(0, len(numbers_list) - 1)
                id = id + numbers_list[random_numbers_list_index]
            elif random_type_list == 2:                                                     # si es 2 iteramos aleatoriamente por la lista de letras mayusculas
                random_letters_list_mayusc_index = randint(0, len(letters_may_list) - 1 )
                id = id + letters_may_list[random_letters_list_mayusc_index]
            else:
                id = id + ''
        print(id)
    for any in range(0, repetitions):
        random_one()

random_user_id(5, 2)
random_user_id(7, 5)
random_user_id(18, 3)
""" output
3DB40
0ZLMR
626dC52
5qha346
S8132Xv
Vm3DgCW
yQ0Wv19
153Dv8pLps245fw9X5
wIcH6941U1UA761N7a
fBTIX01Uu817P3hSlI """
random_user_id(18, 100)
""" output big one:
ebH6v
UDnI8
C2yMmM9
76SPb3S
56Orm4g
mmEy3RS
ROtJG6j
Sfl0RhVxH1GJyYDlJ9
KK5mvK1d4m62e502Qr
rf0A4h2153W7252p1E
6p6jWkgn9xSayAQ1ai
93M9gkueGLtr8K52qp
N5In13DVCK9yix5hOc
0rWv76D9Bu8j1gCNRj
9ZCmQ16M7y4Nru5vwy
KsnOr2seS8y8J5hl16
ZwLoGlbLsH7aO8gfFm
uoW3Wky0PT5VpTcq7g
05sX0oO8C2nHeLJSHu
s4wCL4ekhkMJw58WTC
YLOVa95akdt91lFpI8
4B4gxS5tv44qqtUioq
48cJap9f94227XNIe1
D2dUcdy37vJc4nPcWl
P1pRfMN2FoV4fEbyhY
K680o0jfzAG3xIOg3k
96DzNUMgp2Pa4kizTk
nR28VAd41GnRGbMw8L
u15nWtjA45r021u9EF
y25kT9Lj6pVdYbJ8yA
fIcu2HePSX8a4o62X4
IM1aUc0i2D4QnWg4qc
044nSn3qU8H8lPkRg0
1XbBNOl8fOf6bNj310
FTRlfUe7XE37IOGTZX
8T9Rr68Cz8v2Lv7P26
P4SF669F2J8nb982uD
394inqYVq4JjDLq47N
KGzOuhLuaDej5xC0G1
aqBM2Z8CwH0I7B3yti
G4874L1wZJJRDUKBSh
S2nmSmMq7cEy77LRl8
MelKuoq97GU19HI8Bk
jLq14clyIpUa7OC52y
Wdd1Qba4na7Mbg8G9t
zXD4SrE4wm6657bqc7
hHd5ni7G4c8OjH5g7P
2aO0fFNqklUuP62Pl5
j927QbCZbVJXnY8L08
d0l6r0X1hNs07x3r1X
7hp36zbk2G0kE56x4X
4JbN42N0640xN6f9oW
w4u4j4c06Le1aGwUdg
Iv5ibOpzb04t2DlNNC
EyVhIgfny42V7wVXBu
R0ZQG4EoRV6P09vKVm
2g9ta7tDlu3yeHatg5
7Uge0suW55aTgN1658
1Um2ye81l936OK1OsR
bCUEvR4C110d1mAUiG
WEJCeg67lf2dfdor22
yDfq2FS4E7zipK57Vk
AhqI25ceB8Lpprgl9w
2n37yRaXk5hiXHQpmE
UC62f94blF9F3PE6gs
B67Bfb8K9kchObZHGm
heT0pF3zy14Hrj2Q5K
JMmX49gi2uHIFRL2Ek
1MHWqDZYmgf72lTS3P
UJ0d5P48zO11rd0efc
MskCK5SQ1k46jMz26J
BZxBW0E7rN6d6r1TcJ
03B43LaZO254eW2lb9
sv1AciqbUHidxD5QT0
YY7lJ8hY7GQjb8oSOd
Q2ZzPMoPJHkFPFuIW5
0loUdxZv151UPPafa3
C3kv2dGWKqcHvJ9alS
3PESmnW5zsI5M7Ppeq
0h94mUgesHfe78193E
3q8yJNgPSf2pYCKoYq
7n85Ns25yb4XdCBfy3
Pgc6b1qIhFL220MISU
faU261Hi13A2Y5Npp2
1oT7Wk11udDJEz8258
46vBS5WjUdGaz0SKdb
EgTY9yPLNvc5QOi9Xn
NuxCV4f95P5Dno4IPB
Cn0g3Q7wlmqorcqS0c
cF7p3KCAJ5qTYK9e4g
kFjs1D5jxVzE1ub6vj
p5iMhkJLp30B325hTh
3U5wb79n20PLW2P3GK
283gdnI86Ib0Uj4Mxi
ywMu7Xt6mE2NUqbBpa
Y2tIMl7QOMx136ToXH
Xd7g47SE219Ihv158N
AOZY9hw7yY2o4Tfg4X
E6F5EYP5i8Th9D573L
pJ2kaDon2l78rYD852
08Yrr7e5ph86MP3n71
idFKz5yrgtooGoD4Yu
2A5xcls025WB3gKvjf
di6Q4dr6uKT4fqs868
J1Cf03S1ifonVTdLK2
K3Ih1Zw8KqYN682dw0
6CXRo6zl9tdERce33R
q9JDIeS07P34c271KH
MD8bIA4uz2SdWlwMgS
z2Xy3F75lqvxZ8R8L7 """

# This only takes 0.086 seconds to done. That is incredible