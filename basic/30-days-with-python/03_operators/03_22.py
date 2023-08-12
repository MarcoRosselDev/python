### 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

num_of_years = int(input('Tell me a number of year, please : '))

menute = 60
hours = 60 * menute
day = 24 * hours
year = 365 * day

second_a_year = num_of_years * year
print('seconds of live : ', second_a_year)
# 6 years =  189 216 000 seconds