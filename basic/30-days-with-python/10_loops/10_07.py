### 7. Use for loop to iterate from 0 to 100 and print only even numbers

print('this is with for loop')
for even_number in range(0, 101, 2):
    print(even_number)

print('this is with while loop')

count = 0
while count < 101:
    if count % 2 == 0:
        print(count)
        count = count + 1
    else:
        pass
        count = count + 1

""" output
this is with for loop
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
this is with while loop
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100 """