a = 222
b = 21  #integer
c = 'hari' #string
d = 22.3 #float
print(a + b)


#or
# assigning multiple values:
e , f , g = 121 ,11 , 'ram'
print(e + f)
#multiple variable for 1 value:
h = i = j =787
print(h + i + j)

h = 'orange' ,'apple'
print(h)
# declaration of variable are case senditive

# Pascal Case:
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case:
# Each word is separated by an underscore character:
my_variable_name = "John"

# Camel Case:
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# variables types

value1 = 1  #global variable (declares outside to the fn)

def addition (value2):
    answer = 0  #local variable (declares inside to the fn)
    #or 
    # global value1
    answer = value1 + value2
    print(answer)
addition(21)

def subtraction (value3):
    answer =0  #local variable (declares inside to the fn)
    answer = value1 - value3
    print(answer)
subtraction(21)