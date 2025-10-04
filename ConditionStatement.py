# if...else 
a = 10
if a > 5:
    print('yes')
else:
    print('no')

# in single line
num =2
check = f'{num} is positive' if num >0 else ' 0 is neither + nor -' if num == 0 else f'{num} is negative'
print(check)