class employee:
    def __int__(self, from_date, to_date, employee_name, total_hours, hourly_rate, income_tax_rate, net_pay):
        self.from_date = from_date
        self.to_date = to_date
        self.employee_name = employee_name
        self.total_hours = total_hours
        self.hourly_rate = hourly_rate
        self.income_tax_rate = income_tax_rate
        self.net_pay = net_pay

import re
emp = []
empDic = dict()
totalemp = 0

def addEmployee():
    while True:
        fd = input("Enter from date(dd-mm-yyyy: ")
        x = bool(re.search(r"(%d-%m-%y)", fd))
        if x != True:
            print("No match. Please try again.")
        else:
            break
    while True:
        td  = input("Enter to date(dd-mm-yyyy): ")
        y = bool(re.search(r"(%d-%m-%y)", td))
        if y != True:
            print("No match. Please try again.")
        else:
            break
        en = input("Enter employee name: ")
        th = int(input("Enter total hours: "))
        hr = int(input("Enter hourly rate: "))
        empl = employee(fd,td,en,th,hr,0,0)
        emp.append(empl)
        print("Employee added successfully")

def calculateTaxAndPay():
    for i in range(len(emp)):
        total = emp[i].total_hours * emp[i].hourly_rate
        tax = total * 10 / 100
        emp[i].income_tax_rate = tax
        netpay = total - tax
        emp[i].net_pay = netpay
    print("Salary calculated successfully")

def display():
    print("From Date\tTo Date\t\tEmployee Name\tTotal Hours\tHourly Rate\tIncome Tax Rate\t\tNet Pay")
    for i in range(len(emp)):
        print("%s\t%s\t%s\t%d\t\t%d\t\t%f\t\t%f" %
(emp[i].from_date,emp[i].to_date,emp[i].employee_name,emp[i].total_hours,emp[i].hourly_rate,emp[i].incom_tax_rate,emp[i].net_pay)
              
def totalInDictionary():
    te,th,tt,tnp = totalEmp,0,0,0
    for i in range(len(emp)):
        th = th + emp[i].total_hours
        tt = tt + emp[i].income_tax_rate
        tnp = tnp + emp[i].net_pay
        empDic["total_employee"] = totalEmp
        empDic["total_hours"] = th
        empDic["total_tax"] = tt
        empDic["total_net_pay"] = tnp
        print(empDic)
    
    while True:
        print("1-Add Employee")
        print("2-Calculate Salary")
        print("3-Display Details")
        print("4-Total in Dictionary")
        print("5-Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addEmployee()
            totalEmp = totalEmp + 1
            print()
        elif choice == 2:
            calculateTaxAndPay()
            print()
        elif choice == 3:
            display()
            print()
        elif choice == 4:
            totalInDictionary()
            print()
        elif choice == 5:
            exit()
        else:
            print("Wrong input")
            print()

if __name__ == "__main__":
    main()



 




    
