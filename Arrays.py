# arr = ['volvo' , 'honda' , 'benz' , 'audi']
# arr.append('bmw')
# arr.insert(0,'l')
# arr.remove('honda')
# arr.pop(1)
# print(arr)


class ave():
    def __init__(self,numbers):
        self.numbers = numbers
       
    def average(self):
        total = 0
        for i in self.numbers:
            total +=i
        return int(total/len(self.numbers))
    def print(self):
        ans = self.average()
        print(f'the average : {ans}')
        

obj1 = ave([1,2,3,4,5])
obj1.average()
obj1.print()
print(obj1)
obj2 = ave([10,10,10,10])
obj2.average()
obj2.print()
print(obj2)
