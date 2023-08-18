### 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

challenge = 'I am a teacher and I love to inspire and teach people'
lst = challenge.split(sep=None)
set_lst = set(lst)
print(lst)                      # ['I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people']
print('la cantidad de palabras es : ' ,len(lst))
print('la cantidad de palabras unicas es : ' ,len(set_lst))
# la cantidad de palabras unicas es :  12
# la cantidad de palabras unicas es :  10