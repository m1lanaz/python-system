import random
import csv
from csv import writer

class tasks():
    def __init__(self, taskNumber ,taskName, taskStatus):
        self.taskNumber = taskNumber
        self.taskName = taskName
        self.taskStatus = taskStatus
        
    def getTaskNumber(self):
        return self.taskNumber

    def getTaskName(self):
        return self.taskName
    
    def getTaskStatus(self):
        return self.taskStatus
    
    def setTaskNumber(self):
        return self.taskNumber
    
    def setTaskName(self):
        self.taskName = self.taskName
        
    def setTaskStatus(self):
        self.taskStatus = self.taskStatus
        
    def toString(self):
        taskData = (self.taskNumber + " , " + self.taskName + " , " + self.taskStatus)
        return taskData
    
class listTasks:
    tasks = []
    TestLines = []
    def __init__(self):
        self.tasks = []
        self.TestLines = []
        
    def addTask(self, task):
        with open('tasks.csv', 'a') as f:
            writer_object = writer(f)
            writer_object.writerow(task)
            f.close()
        
    def readFromFile(self):
        with open("tasks.csv", newline='') as file:
            self.TestLines = list(csv.reader(file))

    def taskNum(self):
        randomN1 = str(random.randint(0,9))
        randomN2 = str(random.randint(0,9))
        randomN3 = str(random.randint(0,9))
        randomN4 = str(random.randint(0,9))
        tasNum = "T" + randomN1 + randomN2 + randomN3 + randomN4
        return tasNum

t = listTasks()
t.readFromFile()
print(t.TestLines)
