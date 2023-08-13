### 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

### 4. Print the variable company using _print()_.
print('var company : ',company)

### 5. Print the length of the company string using _len()_ method and _print()_.
print('Lenght of the string company : ',len(company))

### 6. Change all the characters to uppercase letters using _upper()_ method.
result = company.upper()
print(result) # CODING FOR ALL

### 7. Change all the characters to lowercase letters using lower() method.
result = company.lower()
print(result) # coding for all

### 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

capitalize = company.capitalize()
title = company.title()
swapcase = company.swapcase()
print('capitalize : ', capitalize)  # capitalize :  Coding for all
print('title : ', title)            # title :  Coding For All
print('swapcase : ', swapcase)      # swapcase :  cODING fOR aLL