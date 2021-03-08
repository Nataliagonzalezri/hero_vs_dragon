import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))

dragon_max_dmg = 10
hero_max_dmg = 20

try:
    hero_hp = int(input("how many hp does the hero have?"))
except ValueError:
    print("Please use integer numbers")
try:
    dragon_hp = int(input("how many hp does the dragon have?"))
except ValueError:
    print("Please use integer numbers")

# add a While for an infinite block
# here goes the while:

while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    dragon_attack < 11
    hero_hp = hero_hp - dragon_attack
    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    if hero_hp <= 0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break
    hero_attack = random.randint(1, hero_max_dmg)
    hero_attack < 21
    dragon_hp = dragon_hp - hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    if dragon_hp <= 0:
        print("Our valiant hero has slain the dragon!")
        break
    input("Round over. Press any key")