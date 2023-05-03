import os
import sys

#Dictionaries

drinks = {"Ultra Sunshine": 2, "Ultra Black": 3, "Ultra White": 4, "Ultra Paradise": 5, "Ultra Red": 6, "Lewis Hamilton": 7}
print (drinks)

employees = {"Finance": ["Jan", "Michiel", "Lisa"], "HR": ["Naj", "Leihcim", "Asil"], "IT": ["Monster", "Redbull", "Coffee", "Tea"]}
print (employees)

employees['Legal'] = ["Mr.Mister"]
print (employees)

employees.update({"Sales": ["Andy", "Ollie"]})
print (employees)

drinks["Lewis Hamilton"] = 20
print (drinks)

print(drinks.get("Ultra White"))