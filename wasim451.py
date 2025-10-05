class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
p=person("Mohd Wasim",16)
p1=person("Mohd Nadim",19)
p.show()
p1.show()