import math
def multiples(a):
    line = []
   
    for i in range(1,4):
      ans = i * a
      line.append(str(ans))
    print(' '.join(line))
        
multiples(2)
multiples(4)

num = 0
if num ==0:
    print(0)
elif num % 2 !=0:
    print('odd')
elif num % 2 ==0:
    print('even')
    
n = 3
line = []
for i in range(1,n+1):
    ans = 9 * i
    line.append(str(ans))
print(' '.join(line))
    
print(324/18)

row = 5
for i in range(1,6):
    print('*')

a = '  hiiii jj jj'
length = len(a)
ans = ''
for i in range(0,length):
    if a[i] == ' ':
       continue
    ans +=a[i] 
print(ans)       


b = a.strip()
print(b)
def find_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"{root1:.2f}")
    print(f"{root2:.2f}")
    
find_roots(1,5,6)

a = 2

for i in range (2,a+1,2):
    print(i)
    
a = '124'
b = 0  
for i in range(0,len(a)):
    b+=int(a[i])
    print(b)   
     
# s = 4
# d = 1
# for i in range(1,s+1):
#     d*=i
# print(d)
    
num = '2314'
odd = []
even = []
for i in num:
    if int(i)%2==0:
        even.append(i)
    if int(i)%2!=0:
        odd.append(i) 
even.sort()
odd.sort()
print(f'{' '.join(even)} \n{' '.join(odd)}')

n = '348'
j = ''
for i in n:
    j+=i
print(' '.join(j))

row = 3
n = '2'
for i in range(0,row):
    print(n)
   
n =10
for i in range(n,0,-1):
    print(i)
    
num =11
if num <1 or num > 31:
    print('Error') 
elif num in [4,6,9,11]:
    print('30')
elif num==2:
    print('Error')
else:
    print('31')
    
row =5
for i in range(1,row+1):
    print(' ' * (row - i) + '*' * (2*i-1))
    
n = 10
l,r = 2,6
if n in range(l,r+1):
    print('yes')
else:
    print('no')
    
a,b = 2,5
for i in range(a,b):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count += 1
print(count)
    
    
a = 6,2
b = 1,2,3,5,7,2
count = 0
for i in a:
    for j in b:
        if i == j :
            count += 1
if count<0:
    print(0)
print(count-1)

def is_prime(a):
    if a <= 1:
        return f'you cannot enter {a}'
    else:
        for i in range(2, a):
            if a % i == 0:
                return f'not a prime {a} which is divisible by {i}' 
        return f'prime {a}' 
print(is_prime(2))
print(is_prime(122))

a = 4,4
b = 1,3,2,3
count = 0
for i in a:
    for j in b:
        if i == j :
            count += 1
if count<0:
    print(0)
print(count-1)

a,b = 2,4
c = 0.5 * a * b
print(int(c))
        
  
input = 48
power = 1
while power <= input:
    power *=2 
print(power)

a = 123456
b = str(a)
c = ''
d = ''
ans = ''
for i in range(0,len(b),2):
    c +=b[i]
for j in range(1,len(b),2):
    d += b[j]
print(d)
print(c)
maxx = max(c,d)
for k in range(len(maxx)):
    if k < len(d):
        ans += d[k]
    if k < len(c):
        ans += c[k]
print(ans)
        

a = '135'
b = '246'
c = ''
maxx = max(a,b)
for i in range(len(maxx)):
    if i<len(b):
        c += b[i]
    if i<len(a):
        c += a[i]
print(c)
