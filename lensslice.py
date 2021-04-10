# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:20:51 2021
I work at Len’s Slice, a new pizza joint in the neighborhood.
I am going to use your knowledge of Python lists to organize some of my sales data
@author: DELL
"""

toppings=['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices=[2,6,1,3,2,7,2]
num_two_dollar_slices=prices.count(2)
num_pizzas=len(toppings)
print('We sell',num_pizzas,'different kinds of pizza!')
pizzas_and_prices=list(zip(prices,toppings))
print(pizzas_and_prices)
pizzas_and_prices.sort()
print(pizzas_and_prices)
cheapest_pizza=pizzas_and_prices[0][1]
print(cheapest_pizza)
priciest_pizza=pizzas_and_prices[-1][1]
print(priciest_pizza)
pizzas_and_prices.pop(-1)
print(pizzas_and_prices)
pizzas_and_prices.insert(4,[2.5,'peppers'])
print(pizzas_and_prices)
three_cheapest=pizzas_and_prices[0:3]
print(three_cheapest)