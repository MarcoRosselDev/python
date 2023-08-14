### 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

challenge = 'You cannot end a sentence with because because because is a conjunction'
solution = challenge.find('because')
print(solution) # 31

### 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

last_because = challenge.rfind('because')
last_because_index = last_because + len('because ')
print('position last because : ', last_because_index)
# position last because :  55

### 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

slice_challenge = challenge[0:31] + challenge[55:]
print(slice_challenge)
# You cannot end a sentence with is a conjunction