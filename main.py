# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma: \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

numItems = len(names)
randomChoice = random.randint(0, numItems - 1)

personToPay = names[randomChoice]
print(personToPay + " is going to buy the meal today!")
