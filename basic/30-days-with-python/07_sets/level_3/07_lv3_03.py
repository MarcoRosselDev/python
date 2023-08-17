### 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

challenge = 'I am a teacher and I love to inspire and teach people'
lst = challenge.split(sep=None)
print(lst)                      # ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
print('la cantidad de palabras unicas es : ' ,len(lst))
# la cantidad de palabras unicas es :  12