def sum(num:list[int],target:int):
    ans=[]
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                ans.append([i,j])
            return ans

print(*sum([2,7,11,15],9))        

l1=[2,4,3]
l2=[5,6,0]
n1 = int(''.join(map(str,l1[::-1])))
n2 = int(''.join(map(str,l2[::-1])))
tot = n1+n2
print([int(d) for d in str(tot)][::-1])