numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

""" output
0
Next number should be  1
1
Next number should be  2
2
Next number should be  3
3
4
Next number should be  5
5
loop's end
outside the loop
"""