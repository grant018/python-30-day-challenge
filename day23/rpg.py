import time

class Room:
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items

class Player:
    def __init__(self, name, current_room, inventory=None, health=100):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.health = health
        self.attack_power = 25

    def move(self, direction):
        if direction.lower() in self.current_room.exits:
            if self.current_room.exits[direction] != locked_room:
                self.current_room = self.current_room.exits[direction]
                print(f"You have moved into the {self.current_room.name} which can only be described as {self.current_room.description}.")
                if self.current_room.items:
                    for item in self.current_room.items:
                        print(f"In this room is a {item}")
            elif self.current_room.exits[direction] == locked_room and "key" in self.inventory:
                self.current_room = self.current_room.exits[direction]
                self.inventory.remove("key")
                return 1
            else:
                print("This room is locked.")
        else:
            print("There is no exit in that direction.")

    def pick_up(self, item):
        if self.current_room.items:
            if item in self.current_room.items:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You have picked up a {item}")
            elif item == "key" and self.current_room.name == "Game Room":
                if "key" not in self.inventory:
                    self.inventory.append(item)
                    print("You have found the secret key!")
        else:
            print(f"There is no {item} in this room.")

    def show_inventory(self):
        if self.inventory != []:
            print("You have the following items in your inventory:")
            for item in self.inventory:
                print(item)
        else:
            print("Your inventory is empty")

    def attack(self, enemy):
        enemy.health -= self.attack_power
        print(f"You attack the monster and cause {self.attack_power} damage")

class Enemy:
    def __init__(self, current_room, health=50, attack_power=10):
        self.current_room = current_room
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        player.health -= self.attack_power
        print(f"The monster strikes and causes {self.attack_power} damage to you")

hallway = Room("Hallway", "Long creepy hall", {})
kitchen = Room("Kitchen", "Where you prepare food, idiot!", {}, ["blender", "knife"])
bedroom = Room("Bedroom", "This is where your dumbass sleeps", {}, ["sword", "lava lamp"])
living_room = Room("Living Room", "You watch TV and shit in here", {}, ["baseball bat"])
game_room = Room("Game Room", "You like games bitch?", {}, ["pool cue", "tennis racket"])
locked_room = Room("Winner's Circle", "You fucking won bitch", {}, ["trophy"])

hallway.exits = {"west": kitchen, "south":game_room}
kitchen.exits = {"east": hallway, "west": bedroom, "south": living_room}
bedroom.exits = {"east": kitchen}
living_room.exits = {"north": kitchen, "west": locked_room, "east": game_room}
game_room.exits = {"north": hallway, "west": living_room}

def game():
    aladdin = Player("Aladdin", kitchen)
    enemy = Enemy(living_room)

    print("Aladdin wakes up in a kitchen")
    
    while True:
        command = input("\n What do you want to do? ").lower().split()

        if command[0] == "go":
            result = aladdin.move(command[1])
            if result == 1:
                print("You have used the key to unlock the door!")
                print("But there is a monster blocking your path.")
                while True:
                    fight_command = input("Your move. What do you do? ").lower()
                    if aladdin.inventory != []:
                        if fight_command == "attack" and enemy.health > 0:
                            aladdin.attack(enemy)
                            time.sleep(2)
                            if enemy.health <= 0:
                                print("You have defeated the monster!")
                                aladdin.pick_up("trophy")
                                print("You win!")
                                break
                            else:
                                enemy.attack(aladdin)
                                time.sleep(2)
                                if aladdin.health <= 0:
                                    print("The monster has killed you.")
                                    print("Game over")
                                    break
                    else:
                        print("The monster absolutely destroys you since you don't have a weapon")
                        print("Game over")
                        break
                break
            
        elif command[0] == "pick" and command[1] == "up":
            if len(command) == 3:
                aladdin.pick_up(command[2])
            elif len(command) == 4:
                aladdin.pick_up(f"{command[2]} {command[3]}")
            else:
                print("Invalid item selection")
        elif command[0] == "inventory":
            aladdin.show_inventory()
        elif command[0] == "look":
            print(f"You are in the {aladdin.current_room.name}. {aladdin.current_room.description}")
            if aladdin.current_room.items:
                for item in aladdin.current_room.items:
                    print(f"In this room is a {item}")
            else:
                print("There are no items in this room.")
        elif command[0] == "search":
            if aladdin.current_room.name == "Game Room":
                aladdin.pick_up("key")
        elif command[0] == "quit":
            break
        else:
            print("Invalid command. You can say things like 'Go North' or 'Pick Up Sword' / To see your inventory type 'Inventory' / 'Quit' to exit game.")

if __name__ == "__main__":
    game()
