#Ryan Cox
#29/01/15
#store employee details

class employee_details:

    def __init__(self):
        self.employeeName = "-"
        slef.employeeNumber = "-"
        self.hoursWorked = "-"
        self.rateOfPay = "-"

#main program

new_employee_details = employee_details 
        
name = input("Enter the name of the employee: ")
number = input("Enter the number of the employee: ")
hours = input("Enter the hours that the employee worked this week: ")
pay = input("Enter the hourly rate of pay of the employee: ")


employee_details.employeeName = name
employee_details.employeeNumber = number
employee_details.hoursWorked = hours
employee_details.rateOfPay = pay

payslip = []

payslip.append(employee_details)

def display():
    print (" ")
    print("Pay slip")

    print("Name: {0}".format(employee_details.employeeName))

    print("Employee Number: {0}".format(employee_details.employeeNumber))

    print("Hours worked: {0}".format(employee_details.hoursWorked))

    print("rate of pay: {0}".format(employee_details.rateOfPay))
