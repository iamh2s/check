class name ():
    name = 'hari'
    age = 12
    colour = 'white'

obj1 = name()
print(f'my name is {obj1.name}, my age is {obj1.age} and my colour is {obj1.colour}')

# constructor(init fn)

# class details ():
#     def __init__(self,name,age,dob):
#           self.username = name
#           self.userage = age
#           self.userdob = dob
          
#     def print(self):
#         print(f'my name is {self.username} , my age is {self.userage} and my dob is {self.userdob} ')

# obj1 = details(
#     str(input('Enter your name:')),
#     int(input('Enter your age:')),
#     str(input('Enter your Dob:'))
# )
# obj1.print()

# obj2 = details(
#     str(input('Enter your name:')),
#     int(input('Enter your age:')),
#     str(input('Enter your Dob:'))
# )
# obj2.print()

# obj3 = details(
#     str(input('Enter your name:')),
#     int(input('Enter your age:')),
#     str(input('Enter your Dob:'))
# )
# obj3.print()

# class details():
#     def __init__(self,name,age,dob):
#         self.name = name
#         self.age = age
#         self.dob = dob
        
#     def print(self):
#         return f'my name is: {self.name} \n my age is: {self.age} \n my date of birth is: {self.dob}'
        
# obj1 = details('hari' , '12' , '12/2/2004')
# print(obj1.print())
# print(obj1)

        
# class area():
#     def __init__(self,length,breath,radius):
#         self.length = length
#         self.breath = breath
#         self.radius = radius
        
#     def aor(self):
#         print(f'\n area of rectangle is {self.length * self.breath}')
#     def aoc(self):
#         print (f'area of circle is {22/7 * pow(self.radius , 2)}') 
#     def __str__(self):
#         return 'thankyou'
    
# obj1 = area(2,3,100)
# obj1.aor()
# obj1.aoc()
# print(obj1)

class Problem():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def join(self):
        c = ''
        max_length = max(len(self.a), len(self.b))
        for i in range (0,max_length):
              if i < len(self.a):
                 c += self.a[i]
              if i < len(self.b):
                 c += self.b[i]
        return c
    
    def __str__(self):
        return f'the output is :{self.join()}'
            
    
    
    
obj1 = Problem('abc', '123')
print(obj1)
obj2 = Problem('def', '456')
print(obj2)
 
 
def palindrome():
    
    for i in range(9000,10001):
        string = str(i)
        rev = string[::-1]
        
        if string == rev:
            print(f'{string} is equal to {rev} so, it is palindrome')
palindrome()

for i in range(0,11):
    print(i)
    
   
          

  