class Employee:
    eid=0
    name=""
    def getData(self,eid,name):
        self.eid=eid
        self.name=name
    def show(self):
        print("Employee ID=",self.eid)
        print("Employee Name=",self.name)
e=Employee()
e.getData(101,"Kiran")
e.show()
