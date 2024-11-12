print("As salaamu alaikum, welcome to Sunnah Brew! Home of the finest coffee.")

# Name for order
name = input("What is your name for your order?\n")

# No Crackheads allowed!!
if name.lower() == "ben" or name.strip() == "":
    crackhead_status = input("Are you a crackhead? (Yes/No)\n")
    if crackhead_status.lower() == "yes":
        print("You're not welcome here crackhead! Get out before I call the police!!!")
        exit()
else:
    print("Hello " + name + ", thank you for coming in today.\n\n\n")

# Cafe menu
menu = "Black coffee, Espresso, Latte, Tea"
print(f"{name}, what can I get you today? Here is what we are serving:\n{menu}")

order = input()
if order.lower() == "tea":
    print("Ah, need something to relax your mind, ey?")
elif order.lower() == "black coffee":
    print("You must really need a pick me up, ey?")
elif order.lower() == "espresso":
    print("I assume this is for your wife, ey?")
elif order.lower() == "latte":
    print("Feeling a little fancy today, ey?")
else:
    print("Sorry, we don't serve that here.")
    exit()

price = 4

quantity = input("How many would you like?\n")
total = price * int(quantity)

print(f"Thank you, your total is: ${total}")

print(f"Sounds good {name}, I will have your order ready in a moment.")

import time
n = 5
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1

print("Here you go! Thank you for coming into Sunnah Brew. Have a great day.")
