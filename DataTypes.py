# int(numbers)
# float(decimals)
# complex(imaginary part)
import random
# z = 1
# x = 2j
# y = 22.4
# print(z + x) 

print(random.randrange(1,10))

# casting (changing one to another data type)

a = 10
b = str(a)
print(b)
print(type(b))

c =12
d =float(c)
print(d)
print(type(d))


# string
e ='''lorem 
          gopal
ram'''
print(e)  # or ''' 

# get character
name = 'hariharasudhan'
#single char
print(name[2])
#sliding window
print(name[2:])
print(name[2:7])
print(name[:7])

# negative

print(name[-1:])

# reverse
reverse = name[::-1]
print(reverse)


# string modification
username = ' hari hara @sudhan '
print(username.upper())  #caps letter
print(username.lower())  #small letter
print(username.strip())  #removers space
print(username.replace('h','r'))  #replace value
print(username.split('@'))  #create space with denoted symbol, letter etc

x =' '
print(bool(x))

x =200
print(isinstance(x,int))

a = 'guvi'
b = ''
for i in a:
    b +=i
    c =','.join(b)
print(c)
   


    
  