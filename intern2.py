import random

def intro():
    print("Welcome to the Jungle Adventure!")
    print("You find yourself in a dense jungle, surrounded by towering trees and the sounds of wildlife.")
    print("Your goal is to find your way out of the jungle safely.")
    global health
    global inventory
    health = 100
    inventory = []
    start()

def start():
    print("\nYou are at a crossroads. You can go left, right, or straight.")
    print("Health: ", health)
    print("Inventory: ", inventory)
    choice = input("Which way do you want to go? (left/right/straight) ").lower()
    
    if choice == "left":
        river()
    elif choice == "right":
        cave()
    elif choice == "straight":
        village()
    else:
        print("Invalid choice. Try again.")
        start()

def river():
    print("\nYou come across a fast-flowing river.")
    print("You can either try to swim across or look for a bridge.")
    print("Health: ", health)
    print("Inventory: ", inventory)
    choice = input("What do you want to do? (swim/bridge) ").lower()
    
    if choice == "swim":
        print("The current is too strong! You are swept away by the river and lose some health.")
        lose_health(30)
        if health > 0:
            start()
        else:
            game_over()
    elif choice == "bridge":
        print("You find a bridge and safely cross the river.")
        if random.choice([True, False]):
            treasure()
        else:
            start()
    else:
        print("Invalid choice. Try again.")
        river()

def cave():
    print("\nYou find a dark cave.")
    print("You can either enter the cave or continue walking.")
    print("Health: ", health)
    print("Inventory: ", inventory)
    choice = input("What do you want to do? (enter/continue) ").lower()
    
    if choice == "enter":
        print("The cave is full of bats! You are overwhelmed and lose some health.")
        lose_health(20)
        if health > 0:
            start()
        else:
            game_over()
    elif choice == "continue":
        print("You find a hidden path that leads you out of the jungle. You are safe!")
        win()
    else:
        print("Invalid choice. Try again.")
        cave()

def village():
    print("\nYou stumble upon a small village.")
    print("The villagers are friendly and offer to help you.")
    print("Health: ", health)
    print("Inventory: ", inventory)
    choice = input("Do you accept their help? (yes/no) ").lower()
    
    if choice == "yes":
        print("The villagers guide you out of the jungle. You are safe!")
        win()
    elif choice == "no":
        print("You decide to continue on your own but get lost. You never find your way out.")
        game_over()
    else:
        print("Invalid choice. Try again.")
        village()

def treasure():
    print("\nWhile crossing the bridge, you find a hidden treasure chest!")
    print("You found a health potion and a map!")
    inventory.append("health potion")
    inventory.append("map")
    choice = input("Do you want to drink the health potion now? (yes/no) ").lower()
    if choice == "yes":
        print("You drink the health potion and regain some health.")
        gain_health(50)
    start()

def lose_health(amount):
    global health
    health -= amount
    print(f"You lost {amount} health. Current health: {health}")

def gain_health(amount):
    global health
    health += amount
    print(f"You gained {amount} health. Current health: {health}")

def game_over():
    print("\nGame Over. Better luck next time!")
    play_again()

def win():
    print("\nYou win! Congratulations!")
    play_again()

def play_again():
    choice = input("Do you want to play again? (yes/no) ").lower()
    if choice == "yes":
        intro()
    elif choice == "no":
        print("Thank you for playing Jungle Adventure!")
    else:
        print("Invalid choice. Try again.")
        play_again()

# Start the game
intro()


