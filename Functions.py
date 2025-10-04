# function
def printf (fruit,colour):
    print (f'{fruit} is {colour} in colour')

printf('apple','red')
printf('mango','yellow')

# lambda (used for writing fn in single line)
x = lambda a,b : a + b
print(x(2,3))


def add (a,b):
    print(a+b)

add(2,3)

def result (a,b):
    add = lambda c : a + b + c
    print(add(2))

result(2,3)


def area_of_rectangle(length,breath):
    return length * breath

area = area_of_rectangle(2,3)
print('area of rectangle is :',area) 

def area_of_circle(radius):
    return 22/7 * pow(radius , 2)

print(area_of_circle(2))


# recursion
# def add (n):
#     print (n)
#     return add(n+1)
    
# add(5)

def sumofn(number):
    if(number == 1):
        return 1
     
    return number + sumofn(number-1) 

ans = sumofn(4)
print(ans)

add=0
past =0
for i in range (0,10):
    
    add += i
    
    print(add)
   
   
   
   
def addition(a,b):
    c = a+b
    return c

print(addition(2,3))

x = lambda a,b,c : a+b+c 
print(x(1,2,3))