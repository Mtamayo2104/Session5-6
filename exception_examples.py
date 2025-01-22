name = input("what is your name? ")
print("Hello", name)
age = input("How old are you? ")
try:
    age = int(age)
     # u need to specify the value as integer to avoid errors
    # new_age = age / 0
except ValueError:
    print("you are trying to trick me")
    print("better luck next time")
except ZeroDivisionError:
    print("you cant divide by zero")
except:
    print("something unexpected happened")
else:
    print("you were probably born in ", 2024 - age)
finally:
    print("thanks for playing")