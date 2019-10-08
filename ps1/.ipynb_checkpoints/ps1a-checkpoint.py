# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:55:31 2019

@author: asus
"""
"""
House hunting
caculate the months to save enough money to make the down payment of your dream house
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a demical:  "))
total_cost = float(input("Enter the cost of your dream house: "))
portion_down_payment = total_cost*0.25
r = 0.04   #the annual rate of investment reward
monthly_salary = annual_salary/12
current_savings = 0
months = 0
while current_savings < portion_down_payment:
    current_savings += current_savings*(r/12) + monthly_salary*portion_saved
    months += 1
print("Number of months: ", months)