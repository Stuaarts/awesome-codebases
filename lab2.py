# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = [1, 2, 3, 4, 5, 6]

# Error handling for combat strength inputs
try:
    combatStrength = int(input("Enter your combat Strength: "))
    mCombatStrength = int(input("Enter the monster's combat Strength: "))
except ValueError:
    print("Error: Combat Strength must be an integer!")
    exit()

# Rolling for health points
input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Analyze the roll
input("Analyze the roll (Press enter)")
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))
print("--- Phew, you have a healing potion: " + str(not (healthPoints < mCombatStrength) and healingPotion == 1))
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# Weapon array
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

# Roll the dice to choose a weapon
weaponRoll = random.choice(diceOptions)
print(f"You rolled a {weaponRoll}, selecting your weapon...")

# Add weaponRoll to the hero's combat strength
combatStrength += weaponRoll

# Display weapon information
weaponName = weapons[weaponRoll - 1]
print(f"Your weapon is: {weaponName}")

# Conditional messages based on weaponRoll
if weaponRoll <= 2:
    print("You rolled a weak weapon, friend.")
elif weaponRoll <= 4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend!")

# Additional message if the weapon is not Fist
if weaponName != "Fist":
    print("Thank goodness you didn't roll the Fist...")

# Fight simulation
print("\nYou meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your weapon (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength
    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))

