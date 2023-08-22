""" 4. Write different functions which take lists. 
They should calculate_mean, calculate_median, 
calculate_mode, calculate_range, calculate_variance, 
calculate_std (standard deviation). """

# funcion que calcule ma media = sumar cada valor / numero de valores 

def calculate_mean(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum/len(list)
    return print(f"La media de {list} es {mean}")

calculate_mean([1, 3, 5, 2, 4])
# La media de [1, 3, 5, 2, 4] es 3.0
#-----------------------------------------------------------------------
# funcion que devuelva el indice de en medio de la lista

def calculate_median(list):
    median = int(len(list)/2)
    return print(list[median])

calculate_median([1, 3, 5, 2, 4]) # 5
#-----------------------------------------------------------------------
# retorna el valor que mas se repite en la lista

def calculate_mode(list):
    dictionary = {}
    for i in list:
        if dictionary.get(f"currency_{i}") == None:
            dictionary[f"currency_{i}"] = list.count(i)
        else:
            pass
    my_list = []
    for h in dictionary:
        my_list.append(dictionary[h])
    my_list.sort(reverse=True)
    for j in dictionary:
        if dictionary[j] == my_list[0]:
            print(f"The mode of {list} is {dictionary[j]}, with {my_list[0]} repetitions.")

calculate_mode([1, 3, 5, 2, 4, 3, 3, 5])

""" The mode of [1, 3, 5, 2, 4, 3, 3, 5] is 3, with 3 repetitions."""