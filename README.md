Evil_Wizard readme.md

# Fantasy Battle Game

## Overview
A text-based RPG battle simulator where players can choose from different character classes and battle against an evil wizard. The wizard has some crazy abilities, so be prepared for anything unexpected. This project is implemented in Python.

## Features
- Choose from multiple character classes: Warrior, Mage, Archer, and Paladin.
- Engage in battles with an evil wizard who can regenerate health and perform advanced attacks.
- Randomized damage output for more dynamic battles.
- Heal during battle without exceeding the maximum health.

## Character Classes
1. **Warrior**
   - Health: 140
   - Attack Power: 25
2. **Mage**
   - Health: 100
   - Attack Power: 35
3. **Archer**
   - Health: 80
   - Attack Power: 30
4. **Paladin**
   - Health: 150
   - Attack Power: 20
5. **Evil Wizard**
   - Health: 150
   - Attack Power: 15
   - Abilities: Regenerate health, fireball, summon minions, dark blast

## How to Play
1. **Choose Your Character:** Run the game and select your character class by entering the corresponding number.
2. **Enter Battle:** Engage in a battle with the evil wizard. You can choose to attack, use a special ability, heal, or view your stats.
3. **Defeat or Be Defeated:** The battle continues until either the player or the wizard is defeated. The game will display a victory message for the player if the wizard is defeated or a defeat message if the player is defeated.

## Code Structure
- `Character` class: The base class for all characters, including methods for attack, heal, and displaying stats.
- `Warrior`, `Mage`, `Archer`, `Paladin` classes: Inherited from the `Character` class with specific attributes.
- `EvilWizard` class: Inherited from the `Character` class with additional methods for regeneration and advanced attacks.
- `create_character()` function: Prompts the user to choose a character class and returns an instance of the selected class.
- `battle()` function: Controls the flow of the battle, including player actions and wizard's actions.
- `main()` function: Entry point of the game, initializes the player and wizard, and starts the battle.

## Requirements
- Python 3.x

## Running the Game
To run the game, execute the following command in your terminal:

```bash
python path_to_your_script.py
