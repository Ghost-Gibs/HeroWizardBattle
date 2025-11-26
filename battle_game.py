import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.evading = False
        self.shielded = False

    def attack(self, opponent):
        if opponent.evading:
            print(f"{opponent.name} evades the attack!")
            opponent.evading = False
            return
        
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the attack!")
            opponent.shielded = False
            return
        
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 30
        old_health = self.health
        self.health = min(self.health + heal_amount, self.max_health)
        actual_heal = self.health - old_health
        print(f"{self.name} heals for {actual_heal} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.rage_available = True

    def power_strike(self, opponent):
        if opponent.evading:
            print(f"{opponent.name} evades the Power Strike!")
            opponent.evading = False
            return
        
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the Power Strike!")
            opponent.shielded = False
            return
        
        damage = random.randint(35, 45)
        opponent.health -= damage
        print(f"{self.name} unleashes a POWER STRIKE on {opponent.name} for {damage} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def battle_rage(self):
        if self.rage_available:
            self.attack_power += 10
            print(f"{self.name} enters BATTLE RAGE! Attack power increased to {self.attack_power}!")
            self.rage_available = False
        else:
            print(f"{self.name} has already used Battle Rage!")

    def use_special_ability(self, opponent, ability_choice):
        if ability_choice == '1':
            self.power_strike(opponent)
        elif ability_choice == '2':
            self.battle_rage()


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.mana = 100

    def fireball(self, opponent):
        if self.mana >= 30:
            if opponent.evading:
                print(f"{opponent.name} evades the Fireball!")
                opponent.evading = False
                self.mana -= 30
                return
            
            if opponent.shielded:
                print(f"{opponent.name}'s shield blocks the Fireball!")
                opponent.shielded = False
                self.mana -= 30
                return
            
            damage = random.randint(40, 55)
            opponent.health -= damage
            self.mana -= 30
            print(f"{self.name} casts FIREBALL on {opponent.name} for {damage} damage! (Mana: {self.mana})")
            
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"{self.name} doesn't have enough mana! (Current: {self.mana}, Required: 30)")

    def mana_restore(self):
        restore_amount = 40
        old_mana = self.mana
        self.mana = min(self.mana + restore_amount, 100)
        actual_restore = self.mana - old_mana
        print(f"{self.name} restores {actual_restore} mana! Current mana: {self.mana}/100")

    def use_special_ability(self, opponent, ability_choice):
        if ability_choice == '1':
            self.fireball(opponent)
        elif ability_choice == '2':
            self.mana_restore()

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Mana: {self.mana}/100")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=30)

    def quick_shot(self, opponent):
        if opponent.evading:
            print(f"{opponent.name} evades the Quick Shot!")
            opponent.evading = False
            return
        
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the first arrow!")
            opponent.shielded = False
            damage = random.randint(20, 30)
            opponent.health -= damage
            print(f"But the second arrow hits for {damage} damage!")
        else:
            damage1 = random.randint(20, 30)
            damage2 = random.randint(20, 30)
            total_damage = damage1 + damage2
            opponent.health -= total_damage
            print(f"{self.name} fires a QUICK SHOT! Two arrows hit {opponent.name} for {damage1} + {damage2} = {total_damage} damage!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.evading = True
        print(f"{self.name} prepares to EVADE the next attack!")

    def use_special_ability(self, opponent, ability_choice):
        if ability_choice == '1':
            self.quick_shot(opponent)
        elif ability_choice == '2':
            self.evade()


class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)

    def holy_strike(self, opponent):
        if opponent.evading:
            print(f"{opponent.name} evades the Holy Strike!")
            opponent.evading = False
            return
        
        if opponent.shielded:
            print(f"{opponent.name}'s shield blocks the Holy Strike!")
            opponent.shielded = False
            return
        
        damage = random.randint(35, 50)
        opponent.health -= damage
        heal_amount = 15
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} strikes with HOLY LIGHT dealing {damage} damage and healing for {heal_amount} health!")
        
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} raises a DIVINE SHIELD! Next attack will be blocked!")

    def use_special_ability(self, opponent, ability_choice):
        if ability_choice == '1':
            self.holy_strike(opponent)
        elif ability_choice == '2':
            self.divine_shield()


class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        old_health = self.health
        self.health = min(self.health + 5, self.max_health)
        actual_regen = self.health - old_health
        print(f"{self.name} regenerates {actual_regen} health! Current health: {self.health}/{self.max_health}")


def create_character():
    print("\n" + "="*50)
    print("WELCOME TO THE BATTLE ARENA!")
    print("="*50)
    print("\nChoose your character class:")
    print("1. Warrior - High health, strong attacks")
    print("   Abilities: Power Strike, Battle Rage")
    print("\n2. Mage - Lower health, powerful magic")
    print("   Abilities: Fireball, Mana Restore")
    print("\n3. Archer - Balanced stats, ranged attacks")
    print("   Abilities: Quick Shot (double attack), Evade")
    print("\n4. Paladin - Defensive tank, holy powers")
    print("   Abilities: Holy Strike (damage + heal), Divine Shield")
    
    class_choice = input("\nEnter the number of your class choice: ")
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
    print(f"\n{'='*50}")
    print(f"{player.name} VS {wizard.name}")
    print(f"{'='*50}\n")
    
    while wizard.health > 0 and player.health > 0:
        print("\n" + "-"*50)
        print("--- Your Turn ---")
        print("-"*50)
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("\nChoose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                print("\nSpecial Abilities:")
                print("1. Power Strike - Devastating attack")
                print("2. Battle Rage - Increase attack power permanently")
                ability = input("Choose ability: ")
                player.use_special_ability(wizard, ability)
            elif isinstance(player, Mage):
                print("\nSpecial Abilities:")
                print("1. Fireball - Powerful magic attack (30 mana)")
                print("2. Mana Restore - Restore 40 mana")
                ability = input("Choose ability: ")
                player.use_special_ability(wizard, ability)
            elif isinstance(player, Archer):
                print("\nSpecial Abilities:")
                print("1. Quick Shot - Fire two arrows")
                print("2. Evade - Dodge the next attack")
                ability = input("Choose ability: ")
                player.use_special_ability(wizard, ability)
            elif isinstance(player, Paladin):
                print("\nSpecial Abilities:")
                print("1. Holy Strike - Attack and heal yourself")
                print("2. Divine Shield - Block the next attack")
                ability = input("Choose ability: ")
                player.use_special_ability(wizard, ability)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")
            continue

        if wizard.health > 0:
            print(f"\n--- {wizard.name}'s Turn ---")
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print("\n" + "="*50)
            print("DEFEAT!")
            print("="*50)
            print(f"{player.name} has been defeated by {wizard.name}!")
            print("Better luck next time, brave warrior...")
            break

    if wizard.health <= 0:
        print("\n" + "="*50)
        print("VICTORY!")
        print("="*50)
        print(f"{player.name} has defeated the evil {wizard.name}!")
        print("The kingdom is saved! You are a true hero!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)
    print("\n" + "="*50)
    print("Thanks for playing!")
    print("="*50)


if __name__ == "__main__":
    main()
