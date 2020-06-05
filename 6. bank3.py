# this is my file reader program
class Account:
    def __init__ (self,aid,atype,abalance):
        self.aid = aid
        self.atype = atype
        self.abalance = abalance

    def getBalance(self):
        return self.abalance

    def getId(self):
        return self.aid

    def getType(self):
        return self.atype

    def __str__(self):
        return self.aid + "," + self.atype + "," + self.abalance
    
import glob
import csv

accountList = []

allFiles = glob.glob("C:\\data\\python\\Bank\\" + "*.csv")
for file in allFiles:
    print (file)
    with open(file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #next(readCSV) -- project has heading
        # read line and populate object
        for row in readCSV:
            #print(row)
            a = Account (row[0], row[1], row[2])
            print(a)
            accountList.append (a)
print(accountList)

min=10000000000
max=0
# loop object list
for a in accountList:
    balance = int(a.abalance)
    if (balance > int(max)):
        max = balance
    if (balance <int(min)):
        min = balance
print ("min =", min, " max =", max)
