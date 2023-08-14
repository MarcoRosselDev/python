### 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

challenge = 'You cannot end a sentence with because because because is a conjunction'
first_because = challenge.find('because')
print(first_because) # 31

### 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
last_because = challenge.rfind('because') + len('because ')
print(last_because) # 55
slice_challenge = challenge[0:31] + challenge[55:]
print(slice_challenge) # You cannot end a sentence with is a conjunction