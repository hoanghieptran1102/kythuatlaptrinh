# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:55:04 2022

@author: Hiep Tran
"""

annual_salary = 150000
portion_saved = 0
step_portion_saved = 0.0001 
total_cost = 1000000
semiannual_raise = 0.07
soThangToiDa = 36
current_saving = 0
while abs(current_saving - 0.25 *total_cost) > 100:
    current_saving = 0
    portion_saved += step_portion_saved
    salary = portion_saved * annual_salary/12
    invest = current_saving * 0.04/12
    
    print("phan tram tiet kiem", portion_saved)
    for i in range(36):
        if i%6 == 0 and i!= 0:    
            salary += salary * 0.07
            current_saving = salary + invest + current_saving
    print("current_saving", current_saving)
    
  
    
print("Ti le tiet kiem luong = ", portion_saved)



annual_salary = 150000
portion_saved_low = 0
portion_saved_high = 1
total_cost = 1000000
semiannual_raise = 0.07
soThangToiDa = 36
current_saving = 0
so_lan_doan = 1
while abs(current_saving - 0.25 * total_cost) > 100:
    current_saving = 0
    portion_saved = (portion_saved_low + portion_saved_high)/2
    salary =  portion_saved * annual_salary/12
    print("phan tram tiet kiem", portion_saved)
    for i in range (36):
        if i%6 == 0 and i!= 0:
            salary += salary * 0.07
        current_saving = salary + invest + current_saving
    print("current_saving",current_saving)
    if 0.25 * total_cost - current_saving > 0:
        portion_saved_low = portion_saved
    else:
        portion_saved_high = portion_saved
    so_lan_doan += 1
print("ti le tiet kiem luong = ", portion_saved )
print("so lan doan", so_lan_doan)
        