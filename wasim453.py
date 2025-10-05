class rectangle:
    def setDimension(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def showDimension(self):
        print("Length=",self.length)
        print("Breadth=",self.breadth)
    def getArea(self):
        return self.length*self.breadth
c=rectangle()
c.setDimension(2,3)
print("Area is=",c.getArea())