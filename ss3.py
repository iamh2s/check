def is_prime(a):
    for i in range(2,a):
      if a%i == 0:
          return('yes')
    return('no')
print(is_prime(123))
print(is_prime(109))

a = 'fish'
b = 'forhjj'
c = 'friendsh'
common = ''
common2 = ''
for i in a:
    if i in b and i in c and i not in common:
        common+=i
print(common)

store = a + b + c
for j in store:
    if j not in common2:
        common2 += j
print(common2)


a = 'hari'
b = 'gopa/'
c = 'r*m'
ans = ''
count1 = 0
count2 = 0
count3 = 0
a1 = a.replace('a', '@')
a2 = b.replace('a', '@')
a3 = c.replace('a', '@')
store = a1+a2+a3
for i in store:
  if i == '@':
    count1 +=1
  if i =='/':
      count2 +=1
  if i == '*':
      count3 +=1
print(f'the count of @ is {count1} \nthe count of / is {count2} \nthe count of * is {count3} ')

a = 5
for i in range(2,a):
    if a%i==0:
        print(f'{a} is not a prime')
        break
    else:
        print(f'{a} is prime')
        break
 
 
a = 'janaga'
b = 'ponpandeeswari'

common1 = '' 
common2 = '' 

count = 1

print("Repeated characters in a:")
for i in a:
    if a.count(i) > 1 and i not in common1:
        common1 += i
        print(i)

for j in b:
        if b.count(j) > 1 and j not in common2:
         common2 += j
         print(f'{count}.{j}') 
         count+=1
         
a = [1,2,3,4,5]
a.append([12,12])
print(a)
a.extend([123,111])
print(a)
print(dir(a))
b = a.pop()
print(a)
print(b)


a,b,c = 3,4,1   
if (a + b) > c:
    print('yes')
elif (a + c) > b:
    print('yes')
elif (b + c) > a:
    print('yes')
else:
    print('no')
    
a = [4,2]
b = [1,2,3,3]
for i in a:
    if i in b:
        print('yes')
        break
else:
    print('no')
    
a = 'codekata'
ans1 = ''
ans2 = ''
result =''
for i in range(0,len(a)):
    if i%2!=0:
        ans1+=a[i]
    if i%2==0:
        ans2+=a[i]
for j in range(0,len(a)):
    if j<len(ans1):
        result+=ans1[j]
    if j < len(ans2):
        result+=ans2[j]
print(result)
        
a = 99

for i in range(2,a):
    if a%i==0:
        print('yes')
        break
else:
    print('no')
        
        
    