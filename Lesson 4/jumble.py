print("n o t p a l i o")
answer = input("Your answer is: ")

if answer == "optional":
    print("You are correct")
else:
    print("Wrong!")

words = ("laptop", "table", "undefined", "obsess", "compulsory", "admirable")
import random

picked = random.choice(words)
shuffled = list(picked)
random.shuffle(shuffled)
print("Jumble word is:",''.join(shuffled))

answer = input("Your answer is: ")
if answer == picked:
    print("You are correct")
else:
    print("Wrong!")