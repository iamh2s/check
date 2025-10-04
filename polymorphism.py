# class addition(): ##complie time polymorphism##
#     def __init__(self,a=0,b=0,c=0,d=0): ##default argunment
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
    
#     def sum(self):
#         return self.a+self.b+self.c+self.d
    
#     def __str__(self):
#         return f'your ans is: {self.sum()}'
    
# result1 = addition(1,2,3)
# print(result1)
# result1 = addition(1,2)
# print(result1)
# result1 = addition(2)
# print(result1)

# class addition():
#     def __init__(self,value):
#         self.value = value
        
    
#     def adding_all_numbers(self):
#         num = 0
#         for i in self.value:
#             num += i
#         return num
        
#     def __str__(self):
#         return f'answer:{self.adding_all_numbers()}'
    

# a = int(input())
# result1 = addition(a) #([1,2,3,4,5])

def add(a=None, b=None, c=None):
    if a is None and b is None and c is None:
        return 'please enter values'
    elif a is not None and b is None and c is None:
        return a
    elif a is not None and b is not None and c is None:
        return a + b
    else:
        return a + b + c

print(add())        
print(add(1))       
print(add(1,2))     
print(add(1,2,3))   

class calculation():
    def __init__(self,length=0,breath=0,radius=0):
        self.length = length
        self.breath = breath
        self.radius = radius
    def area_of_rectangle(self):
        return f'area of rectangle:{self.length * self.breath}'
    def area_of_circle(self):
        return f'area of circle:{2* 22/7 * self.radius**2}'
obj1 = calculation(2,3,4)
print(obj1.area_of_rectangle())
print(obj1.area_of_circle())

class sum():
    def __init__(self,a=0,b=0,c=0,d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def addition(self):
        return f'addition:{self.a + self.b + self.c + self.d}'
    
    def subtraction(self):
        return f'subtraction:{self.a - self.b - self.c - self.d}'
    
    def __str__(self):
        return f'{self.addition()}\n{self.subtraction()}'
    
obj1 = sum()
print(obj1)

print('hii')
print('hello how are you')


print('i am fine')
print('what about you') 