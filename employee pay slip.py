#Ryan Cox
#29/01/15
#store employee details

class employee_details:

    def __init__(self):
        self.employeeName = "-"
        slef.employeeNumber = "-"
        self.hoursWorked = "-"
        self.rateOfPay = "-"
        self.totalPay = "-"

#main program

new_employee_details = employee_details 
        
name = input("Enter the name of the employee: ")
number = input("Enter the number of the employee: ")
hours = int(input("Enter the hours that the employee worked this week: "))
pay = float(input("Enter the hourly rate of pay of the employee: "))


employee_details.employeeName = name
employee_details.employeeNumber = number
employee_details.hoursWorked = hours
employee_details.rateOfPay = pay
employee_details.totalPay = pay*hours

payslip = []

payslip.append(employee_details)

def stars():

    s = "*"

    numberOfStars = s * 40
       

    return s, numberOfStars



def display(s, numberOfStars):

    print(" ")

    print (numberOfStars)    
    
    print("*Pay slip{0: <33}".format(s))
    
    print("*{0: <38}*".format(" "))

    print("*Name: {0: <32}*".format(employee_details.employeeName))

    print("*Employee Number: {0}".format(employee_details.employeeNumber))

    print("*Hours worked: {0}".format(employee_details.hoursWorked))

    print("*Rate of pay: {0}".format(employee_details.rateOfPay))
    
    print("*{0: <38}*".format(" "))

    print("*total pay: {0}".format(employee_details.totalPay))

    print(numberOfStars)

##main program

s, numberOfStars = stars()
display(s, numberOfStars)
