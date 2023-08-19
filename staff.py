import random
import csv
from csv import writer

class listStaff:
    fileName = "staff.csv"
    TestLines = []
    def __init__(self):
        self.fileName = "staff.csv"
        self.TestLines = []
        
    def readFromFile(self):
        with open("staff.csv", newline='') as file:
            self.TestLines = list(csv.reader(file))

class staffModification():
    
    def customerNum(self):
        randomN1 = str(random.randint(0,9))
        randomN2 = str(random.randint(0,9))
        randomN3 = str(random.randint(0,9))
        randomN4 = str(random.randint(0,9))
        StaffNum = "S" + randomN1 + randomN2 + randomN3 + randomN4
        return StaffNum
    
x = listStaff()
x.readFromFile()
y = x.TestLines
print(y[0][0][1:5])
print(int(y[0][0][1:5]) - 4)