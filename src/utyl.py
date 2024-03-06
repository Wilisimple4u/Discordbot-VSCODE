# utyl.py

import random
import time

item = [
    "water is good",
    "throw your self",
    "When you tossed your salad",
    "my computer is a potato it makes chips",
    "I am the milkman my milk is delicious"
]

def get_item()-> str:
    """returns random response from list"""
    #load_item()
    return random.choice(item)

def add_item(joke: str) -> None:
    item.append(joke)
    #save:item()

def load_item():
    item = "lastet inn"

def save_item():
    item = "lagret"

def do_roast(name, age):
    roasts = [
        f"Hvem er {age} år og hører på justin Bieber?",
        f"Hva står på 2 bein og bråker i timen?",
    ]

    print(random.choice(roasts))
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(name + "!!!!!")