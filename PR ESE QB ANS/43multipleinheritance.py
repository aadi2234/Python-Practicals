#43.	Write a Python program to implement multiple inheritance assuming suitable data.
class Test:
    def getTest(self):
        self.t1=int(input("Enter Test-1 Mark:"))
        self.t2=int(input("Enter Test-2 Mark:"))
    def putTest(self):
        print("Test Marks:","Test-1=",self.t1,"Test-2=",self.t2)
class MicroProject:
    def getMp(self):
        self.mpmark=int(input("Enter Microproject Marks:"))
    def putMp(self):
        print("Microproject Marks:",self.mpmark)
class Result(Test,MicroProject):
    def disp(self):
        self.putTest()
        self.putMp()
        self.totaltest=(self.t1+self.t2)/2.0
        self.avg=(self.totaltest+self.mpmark)
        print("Average Total Marks(outoff 30):",self.avg)
r=Result()
r.getTest()
r.getMp()
r.disp()