class details():
    def __init__(self,name,age,place):
        self.name = name #public
        self.__age = age #private
        self.place = place #public
     
    #getter    
    def printing_age(self):
        return f'my age is:{self.__age}'
     
    #setter
    def update_age(self,age):
          self.__age = age
        
    def __str__(self):
        return(f'my name is:{self.name}\nmy age is: {self.__age}\nmy place is: {self.place}')
        
        
detail1 = details('hari',12,'mdu')
# print(detail1.__age)
print(detail1.name)
print(detail1.printing_age())
print(detail1)

detail2 = details('gopal',22,'mdu')
print(detail2)

detail2.update_age(11)
print(detail2)
detail2.name = 'ram'
print(detail2)
