row = 5
for i in range(1,row+1):
    print(' ' * (row - i) + '*' * (2 * i -1))
    
for i in range(1,row+1):
    print('*')
        
    
def big(a,b,c):
    if a > b and a > c:
        return f'{a} is greater'
    elif b > a and b > c:
        return f'{b} is greater' 
    elif c > a and c > b:
        return f'{c} is greater'
    else:
        return 'try another different numbers'
    
print(big(1,2,2))
print(big(1,2,5))
print(big(1,2,0))

class biggest_number():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def find(self):
           if self.a > self.b and self.a > self.c:
              return f'{self.a} is greater class'
           elif self.b > self.a and self.b > self.c:
              return f'{self.b} is greater class' 
           elif self.c > self.a and self.c > self.b:
              return f'{self.c} is greater class'
           else:
              return 'try another different numbers'

obj1 = biggest_number(1,2,3)
print(obj1.find())
obj2 = biggest_number(1,19,3)
print(obj2.find())
obj3 = biggest_number(10,2,3)
print(obj3.find())

row = 5
for i in range(1,row+1):
    print(' ' * (row-i) + '*' * (2 * i - 1 ) )