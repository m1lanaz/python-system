import random
import csv
from csv import writer
class order:
    def __init__(self, customerNum, orderType, orderID ,price, status):
        self.customerNum = customerNum
        self.orderType = orderType
        self.orderID = orderID 
        self.price = price
        self.status = status
        
    def getCustomerNum(self):
        return self.customerNum 
        
    def setCustomerNum(self):
        self.customerNum = customerNum
        
    def getOrderType(self):
        return self.orderType
        
    def setOrderType(self):
        self.orderType = orderType
        
    def getOrderID(self):
        return orderID
        
    def setOrderID(self):
        self.orderID = orderID
        
    def getPrice(self):
        return price 
        
    def setPrice(self):
        self.price = price
        
    def getStatus(self):
        return status
        
    def setStatus(self):
        self.status = status
        
    def toString(self):
        allAccountData = (self.customerNum+" , "+self.orderType+" , "+self.orderID+","+self.price+" , "+self.status)
        return allAccountData
    
    
  
class listOrders:
    orders = []
    lines = []
    def __init__(self):
        self.orders = []
        self.lines = []
        
    def addTask(self, order):
        with open('orders.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow(order)
            f.close()
        
    def readFromFile(self):
        with open("orders.csv", newline='') as file:
            self.lines = list(csv.reader(file))
             
              
def orderTypePrice(orderTypeInput):
    if orderTypeInput == '1':
        return 100
    elif orderTypeInput ==  '2':
        return 60
    elif orderTypeInput == '3':
        return 200
    elif orderTypeInput == '4':
        return 120
    elif orderTypeInput == '5':
        return 80
    else:
        return False
    
    
def orderType(orderTypeInput):
    if orderTypeInput == '1':
        return 'FY Career reading'
    elif orderTypeInput ==  '2':
        return 'HY career reading'
    elif orderTypeInput == '3':
        return 'FY life reading'
    elif orderTypeInput == '4':
        return 'HY life reading'
    elif orderTypeInput == '5':
        return 'FY love reading'
    else:
        return False
        
class orderModification():
    
    def orderNum(self):
        randomN1 = str(random.randint(0,9))
        randomN2 = str(random.randint(0,9))
        randomN3 = str(random.randint(0,9))
        randomN4 = str(random.randint(0,9))
        orderNum = "O" + randomN1 + randomN2 + randomN3 + randomN4
        return orderNum
    

