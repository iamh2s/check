# creation
fruits = ['apple' , 'orange' , 'mango' , 'papaya' , 'grapes' , 'cherry' , 'lechy' , 'pineapple' , 'greenapple']
print(fruits)
print(fruits[-3:])
print(fruits[::-1])
print(fruits[0:9:3])
print(fruits[0:8])

# conversion of list

a = 'hii' , 22 , True
print(list(a))

b = ('hii' ,'hii')
print(b)

# changing list items

fruits[2] = 'banana'
print(fruits)

#range of changing values
fruits [0:2] = 'watermelon' , 'tomato'
print(fruits)

# using loop
for i in fruits:
    print(i)
