class Sample:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y

sample=Sample(3, 5)
solution=sample.add()
print(solution)