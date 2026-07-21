# Q3. Inheritance, Polymorphism, Composition, OOP Design
# Problem Statement
# Title: Employee Payroll Management System
# Description
# Develop a payroll management system using Object-Oriented Programming principles.
# The system consists of one base class and three derived classes.

# Base Class
# Employee
# Attributes
# . emplloyee_id
# . name
# Method
# calculate_sallary()
# This method should be overridden by all child classes.

# Derived Classes
# FullTimeEmployee
# Additional Attribute
# monthly_salary
# Salary Calculation
# Salary = monthly_salary

# PartTimeEmployee
# Additional Attributes
# Ihours_worked
# hourly_rate
# Salary Calculation
# Salary = hours_worked x hourly_rate

# ContractEmployee
# Additional Attributes
# project_amount
# bonus
# Salary Calculation
# Sallary = project_amount + bonus

# Payroll Class
# Create another class named Payroll.
# It should contain
# employees
# (a list of Employee objects)
# Implement the following methods.

# add_employee(employee)
# Adds an employee to the payroll.
# generate_payroll()
# Display salary detaills iin the following format.
# Employee ID : E101
# Name : Alice
# Salary: R60000

# Employee ID : E102
# Name : Bob
# Sallary: 418000

# Finally display
# Total Payroll = ₹128000

# Test Data
# Create the following employees.
# Full Time

# ID: E101
# Name : Anand
# Salary: 60000

# Part Time

# ID : E102
# Name : Iksha
# Hours : 120
# Hourly Rate : 150

# Contract

# ID: E103
# Name : Chinmayi
# Project Amount : 45000
# Bonus : 5000
# Add all employees to Payroll.
# Generate payroll.

# Requirements
# . Use inheritance.
# Override calculate_salary().
# . Store all employees inside one list.
# . Use polymorphism while generating payroll.
# . Do not use if isinstance() anywhere in the solution.

from typing import override
class Employee:
    def __init__(self,employee_id,name):
        self.employee_id=employee_id
        self.name=name
    
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self,employee_id,name,monthly_salary):
        super().__init__(employee_id,name)
        self.monthly_salary=monthly_salary
    
    @override
    def calculate_salary(self):
        salary=self.monthly_salary
        return salary

class PartTimeEmployee(Employee):
    def __init__(self,employee_id,name,hours_worked,hourly_rate):
        super().__init__(employee_id,name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate
    
    @override
    def calculate_salary(self):
        salary=self.hours_worked*self.hourly_rate
        return salary
        
        
class ContractEmployee(Employee):
    def __init__(self,employee_id,name,project_amount,bonus):
        super().__init__(employee_id,name)
        self.project_amount=project_amount
        self.bonus=bonus
    
    @override
    def calculate_salary(self):
        salary=self.project_amount+self.bonus
        return salary
        
        
class Payroll():
    def __init__(self):
        self.emp = [] 
        
    def add_employee(self,empp):
        self.emp.append(empp)
        
    def generate_payroll(self):
        
        totalpayroll=0
        for i in self.emp:
            salary=i.calculate_salary()
            print("\n=========================")
            print("Employee ID:",i.employee_id)
            print("Employee Name:",i.name)
            print("Employee Salary:",salary)
            totalpayroll=totalpayroll+salary
            print("=========================")
        print("Total Payroll: ",totalpayroll)
        print("=========================\n")
        
        

full=FullTimeEmployee("E101", "Anand", 60000)
part=PartTimeEmployee("E102","Iksha",120,150)
contract=ContractEmployee("E103","Chinmayi",45000,5000)
pay=Payroll()
pay.add_employee(full)
pay.add_employee(part)
pay.add_employee(contract)
pay.generate_payroll()