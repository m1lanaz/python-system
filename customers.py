import random
import csv
from csv import writer

class customerProfile():
    def __init__(self,customerNum, firstName, surName, phoneNum, DOB, TOB):
        self.customerNum = customerNum
        self.firstName = firstName
        self.surName = surName
        self.phoneNum = phoneNum
        self.DOB = DOB
        self.TOB = TOB

    def getFirstName(self):
        return self.firstName
        
    def setFirstName(self):
        self.firstName = firstName
        
    def getSurName(self):
        return self.surName
    
    def setFirstName(self):
        self.surName = surName
            
    def getCustomerNum(self):
        return self.customerNum
        
    def setCustomerNum(self):
        self.customerNum = customerNum
            
    def getPhoneNum(self):
        return self.phoneNum
        
    def setPhoneNum(self):
        self.phoneNum = phoneNum
            
    def getDOB(self):
        return DOB
            
    def setDOB(self):
        self.DOB = DOB
            
    def getTOB(self):
        return TOB
        
    def setTOB(self):
        self.TOB = TOB
            
    def toString(self):
        allAccountData = (self.customerNum+","+self.firstName+","+self.surName+","+self.phoneNum+","+self.DOB+","+self.TOB)
        return allAccountData       
      
      
      
class listCustomerProfile:
    profiles = []
    fileName = "customerProfiles.csv"
    TestLines = []
    def __init__(self):
        self.profiles = []
        self.fileName = "customerProfiles.csv"
        self.TestLines = []
        
    def addCustomer(self, customer):
        self.customer.toString()
        with open('customerProfiles.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow(self.customer)
            f.close()
        
    def readFromFile(self):
        with open("customerProfiles.csv", newline='') as file:
            self.TestLines = list(csv.reader(file))

class customerModification():
    
    def customerNum(self):
        randomN1 = str(random.randint(0,9))
        randomN2 = str(random.randint(0,9))
        randomN3 = str(random.randint(0,9))
        randomN4 = str(random.randint(0,9))
        cusNum = "C" + randomN1 + randomN2 + randomN3 + randomN4
        return cusNum
    