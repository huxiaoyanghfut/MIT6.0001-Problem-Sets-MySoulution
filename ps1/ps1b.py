# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:21:54 2019

@author: asus
"""

"""
House hunting with a raising salary
caculate the months to save enough money to make the down payment of your dream house  
with a raising salary

"""
annual_salary0 = float(input("Enter your annual salary: ")
                       )  # input the inital annual salary
portion_saved = float(
    input("Enter the percent of your salary to save, as a demical:  "))
semi_annual_raise = float(
    input("Enter the semi-annual raise, as a demical:  "))
total_cost = float(input("Enter the cost of your dream house: "))
portion_down_payment = total_cost*0.25
r = 0.04  # the annual rate of investment reward
monthly_salary0 = annual_salary0/12
current_savings = 0
months = 0
times_of_raise = 0
while current_savings < portion_down_payment:
    monthly_salary = monthly_salary0*(1+semi_annual_raise)**times_of_raise
    print(monthly_salary)
    current_savings += current_savings*(r/12) + monthly_salary*portion_saved
    months += 1
    times_of_raise = (months - 1) // 6
    print(times_of_raise)
print("Number of months: ", months)
print(type(current_savings))
