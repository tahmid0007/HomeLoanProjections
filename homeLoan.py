# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:38:11 2022

@author: mthossain
"""
import matplotlib.pyplot as plt


class homeLoan():
    def __init__(self, loan = 427000, rate = 0.0299, repay_frequency = 14, interest_frequency = 30, repayment = 831.0):
        self.loan = loan
        self.rate = rate
        self.repay_frequency = repay_frequency
        self.interest_frequency = interest_frequency
        self.repayment = repayment
        self.interest_cumulitive = 0
        self.year = [0]
        self.loan_on_year = [loan]
        
    def plot_loan(self):
        plt.plot(self.year, self.loan_on_year)
        plt.xlabel('YEAR')
        plt.ylabel('LOAN')
        plt.title('My first graph!')
        return plt
        
    def current_loan(self, after_x_days = None):
              
        for x_day in range(1, after_x_days):
            #if self.loan < 0: break
            if x_day % self.repay_frequency == 0:
                self.loan -= self.repayment
                
            self.interest_cumulitive += ((self.loan * self.rate) / 365.0)
            
            if x_day % self.interest_frequency == 0:
                 self.loan += self.interest_cumulitive
                 self.interest_cumulitive = 0
            if x_day % 365 == 0:
                self.year.append(x_day / 365)
                self.loan_on_year.append(self.loan)
            
        print(f"Current loan after {after_x_days/363} yrs is: {int(self.loan)} $")
        return self.plot_loan()
        
    def when_zero(self, my_plt):
        x_day = 1
        while True:
            #if x_day > 731: break
            if self.loan < 0: break
            if x_day % self.repay_frequency == 0:
                self.loan -= self.repayment
                
            self.interest_cumulitive += ((self.loan * self.rate) / 365.0)
            
            if x_day % self.interest_frequency == 0:
                 self.loan += self.interest_cumulitive
                 self.interest_cumulitive = 0
            if x_day % 365 == 0:
                self.year.append(x_day / 365)
                self.loan_on_year.append(self.loan)
            x_day += 1
            
        print(f"Current loan after {x_day/363} yrs is: {int(self.loan)} $")
        my_plt.plot(self.year, self.loan_on_year)
        my_plt.show()
                

if __name__ == "__main__":
    obj = homeLoan(loan = 408000, rate = 0.04, repay_frequency = 14, interest_frequency = 30, repayment = 900)
    my_plt = obj.current_loan(after_x_days = 10870)  #10870
    
    obj_zero = homeLoan(loan = 408000, rate = 0.07, repay_frequency = 14, interest_frequency = 30, repayment = 1500)
    obj_zero.when_zero(my_plt)       
        

