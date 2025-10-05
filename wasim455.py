class Team:
    def __init__(self):
        self.teamMemeberNames=[]
    def InputMember(self):
        print("Enter the name members seprated by comma")
        self.teamMemeberNames=input().split(',')
    def ShowMember(self):
        for i in self.teamMemeberNames:
            print(i)
p=Team()
p.InputMember()
p.ShowMember()