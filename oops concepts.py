class Doctor:
    def __init__(self,name,specilization):
     self.name=name
     self.specilization =specilization
    def doSurgery (self):
       print(self.name,'is maintaing the surgery')
d1=Doctor('priya','cordilogist')
d2=Doctor('sneah','ent')
d3=Doctor('ramu','ent2')
d1.doSurgery()
d2.doSurgery()
d3.doSurgery()

