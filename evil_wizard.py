import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        min_damage = int(self.attack_power * 0.8)
        max_damage = int(self.attack_power * 1.2)
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} heals for {amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def advanced_attack(self, opponent):
        ability = random.choice(["fireball", "summon_minions", "dark_blast"])
        if ability == "fireball":
            damage = random.randint(20, 40)
            opponent.health -= damage
            print(f"{self.name} casts a fireball at {opponent.name} for {damage} damage!")
        elif ability == "summon_minions":
            minion_count = random.randint(1, 3)
            print(f"{self.name} summons {minion_count} minions to attack {opponent.name}!")
            for _ in range(minion_count):
                damage = random.randint(5, 10)
                opponent.health -= damage
                print(f"A minion attacks {opponent.name} for {damage} damage!")
        elif ability == "dark_blast":
            damage = random.randint(15, 30)
            opponent.health -= damage
            print(f"{self.name} uses dark blast on {opponent.name} for {damage} damage!")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            pass  # Implement special abilities
        elif choice == '3':
            heal_amount = 20  # Example heal amount
            player.heal(heal_amount)
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.advanced_attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            print("You fought bravely, but the Dark Wizard's power was too great. Better luck next time!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
        print("Congratulations! You have triumphed over the Dark Wizard and saved the realm!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
