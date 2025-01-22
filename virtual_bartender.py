from random import choice
drinks = ["gin", "vodka", "whiskey", "rum", "tequila", "absinthe", "sake"]
#print(choice(drinks))
name = input("I am a virtual bartender, What is your name?")
legal = False

try:
    age = input("What is your age? ")
    age = int(age)
    country = input("where are you from? ")
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "luxembourg":
        legal = True
except ValueError:
    print("Dont play games with me")

if legal:
        print("Dear", name, "it is my pleasure to serve you", choice(drinks))
else:
        print("Dear", name, "unfortunately I can not serve you")



