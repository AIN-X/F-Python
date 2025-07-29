#       Python - String Concatenation

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> String Concatenation <<<<<<<<<<<<<<<<<<<<<<<<<\n')

a = 'Ashraful '
b = 'Islam'
c = a + b
print(c)

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> String Format <<<<<<<<<<<<<<<<<<<<<<<<<\n')

age = 25
txt = "I am Ashraful and I am " + str(age)
print(txt)

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> F-Strings <<<<<<<<<<<<<<<<<<<<<<<<<\n')

age = 25
txt = f"I am Ashraful Islam and I am {age}"
print(txt)

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> Placeholders and Modifiers <<<<<<<<<<<<<<<<<<<<<<<<<\n')

price = 50
book = f"The book price is {price} dollar"
print(book)

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> Format to 2 Decimal Places <<<<<<<<<<<<<<<<<<<<<<<<<\n')

price = 50
book = f"The book price is {price:.2f} dollar"
print(book)

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>> Expression in F-String <<<<<<<<<<<<<<<<<<<<<<<<<\n')

book = f"The book price is {20 * 25} dollar"
print(book +"\n")
