import math 

a,b = 37,-73
ans = ''
while b !=0:
    a , b = b , a%b
    ans = str(a).replace("-","")
print(ans)

a, b = 56, 64
sa , sb = str(a),str(b)
a = sa.zfill(max(len(sa),len(sb)))
b = sb.zfill(max(len(sa),len(sb)))
ans = ''
for i in range(len(sa)):
    ans += str((int(a[i]) + int(b[i])) % 10)
print(ans)

