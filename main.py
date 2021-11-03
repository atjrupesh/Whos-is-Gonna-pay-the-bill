# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num_items = len(names)
random_tip=random.randint(0, num_items-1)

person_will_pay=names[random_tip]
print(person_will_pay + " is going to buy the meal")



# tip = random.choice(names)
# print(f"{tip} is going to buy meal today")
