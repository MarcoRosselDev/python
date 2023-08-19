### 8. Use for loop to iterate from 0 to 100 and print only odd numbers

print('with for loop')
for odd in range(1, 100,2):
    print(odd)

print('with while loop')
odd_num = 0
while odd_num < 100:
    if odd_num % 2 != 0:
        print(odd_num)
        odd_num = odd_num + 1
    else:
        odd_num = odd_num + 1
        pass

""" output
with for loop
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
with while loop
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99  """