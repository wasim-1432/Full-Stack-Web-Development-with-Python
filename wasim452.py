class Circle:
    def set(self,radius):
        self.radius=radius
    def get(self):
        return self.radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
c=Circle()
c.set(3)
print(c.getArea())