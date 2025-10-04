# while loop
# odd nos between 1 to 20
i = 0
while i<20:
    i+=1
    print(i)
    i+=1
else:
    print('')
    print('thankyou')
    print('')
    
    
# for loop
for i in range(1,21,2):
    print(i)
else:
    print('')



fabi = 0
for i in range(0,10):
    fabi +=i
    print(fabi)
    
a = 'hari'
b = len(a)
c = ''
for i in range(b-1,-1,-1):
    c += a[i]     #c = c + a[i]
print(c)
    
print(a[::-1])

d=''
for i in range(0,b):
    d = a[i] + d
print(d)