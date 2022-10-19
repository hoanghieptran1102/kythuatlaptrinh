# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:58:22 2022

@author: Hiep Tran
"""


annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: ")) 
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
thang = 0
current_saving = 0
while  current_saving < 0.25 * total_cost :
    thang += 1
    salary = portion_saved * annual_salary/12
    invest = current_saving * 0.04/12
    current_saving = salary + invest + current_saving
    if thang %6 == 0:
       annual_salary = annual_salary *( 1 + semi_annual_raise )
print(thang)

