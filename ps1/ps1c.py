# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 00:03:34 2019

@author: timeshell
"""
"""
House Hunting in 3 years
caculate the best saving rate to make the down payment of your dream house
"""
annual_salary0 = float(input("Enter your annual salary: ")
                       )  # input the inital annual salary
semi_annual_raise = 0.07
total_cost = 1000000
portion_down_payment = total_cost*0.25
r = 0.04  # the annual rate of investment reward
monthly_salary0 = annual_salary0/12
current_savings = 0
times_of_raise = 0
low = 0
high = 10000
portion_saved = (low+high)/2
steps_search = 0
if annual_salary0 < 100000:
    print("It is not possible to pay the down payment in three years.")
else:
    while abs(current_savings-portion_down_payment) >= 0.1:
        steps_search += 1
        current_savings = 0
        for months in range(36):
            monthly_salary = monthly_salary0 * \
                (1+semi_annual_raise)**times_of_raise
            current_savings += current_savings * \
                (r/12) + monthly_salary*portion_saved/10000
            times_of_raise = (months - 1) // 6

        if current_savings <= portion_down_payment:
            low = portion_saved
        else:
            high = portion_saved
        portion_saved = (high+low)/2
    print("portion_down_payment:", current_savings)
    print("best saving rate:", portion_saved/10000)
    print("steps in bisection search:", steps_search)
