

class MySet:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    
    def __add__(self, m):
        return (self.a * m.a, self.b+m.b)
        

    

A = MySet(4,8)

B = MySet(2,9)

# print(B.add())

print(A+B)
print(A.__dict__)