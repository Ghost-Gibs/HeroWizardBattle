# Battle Arena - Turn-Based RPG Game

## Overview
A beginner-friendly Python turn-based battle game where players create hero characters to fight against the Evil Wizard. This project demonstrates Object-Oriented Programming (OOP) principles including inheritance, polymorphism, and encapsulation.

## Purpose
Educational project for learning:
- Python OOP concepts
- Class inheritance and method overriding
- Turn-based game logic
- Interactive menu systems
- Random gameplay mechanics

## Current Features
✅ Four playable character classes:
  - **Warrior**: High health (140 HP), strong attacks (25 ATK)
    - Power Strike: Devastating attack (35-45 damage)
    - Battle Rage: Permanent attack power increase (+10 ATK)
  
  - **Mage**: Lower health (100 HP), powerful magic (35 ATK)
    - Fireball: High damage spell (40-55 damage, costs 30 mana)
    - Mana Restore: Restore 40 mana points
  
  - **Archer**: Balanced stats (110 HP, 30 ATK)
    - Quick Shot: Fire two arrows (20-30 damage each)
    - Evade: Dodge the next incoming attack
  
  - **Paladin**: Defensive tank (130 HP, 22 ATK)
    - Holy Strike: Deal damage (35-50) and heal self (15 HP)
    - Divine Shield: Block the next attack completely

✅ Randomized attack damage (80%-120% of base attack power)
✅ Healing system that respects max health cap
✅ Turn-based battle system with menu options
✅ Evil Wizard boss with health regeneration (+5 HP per turn)
✅ Victory and defeat messages

## How to Play
1. Run the game: `python battle_game.py`
2. Choose your character class (1-4)
3. Enter your character's name
4. Battle the Evil Wizard using:
   - Attack: Basic attack with randomized damage
   - Special Abilities: Two unique abilities per class
   - Heal: Restore 30 HP (max health cap)
   - View Stats: Check current health and stats

## Project Structure
```
battle_game.py - Main game file with all classes and game logic
replit.md - Project documentation
.gitignore - Python ignore patterns
```

## Recent Changes
- 2025-11-26: Initial project setup
  - Created complete battle game with all four character classes
  - Implemented randomized attack damage system
  - Added unique abilities for each class
  - Built turn-based battle system with interactive menu
  - Added healing mechanic with max health cap
  - Implemented Evil Wizard with regeneration ability

## Architecture
- **Base Class**: `Character` - Contains common attributes and methods
- **Hero Classes**: `Warrior`, `Mage`, `Archer`, `Paladin` - Inherit from Character
- **Enemy Class**: `EvilWizard` - Inherits from Character with regeneration
- **Game Functions**: 
  - `create_character()` - Character selection menu
  - `battle()` - Main battle loop
  - `main()` - Game entry point

## Future Enhancements
- Multiple difficulty levels
- Experience points and leveling system
- Inventory system for potions and equipment
- Additional enemy types
- Save/load game functionality
