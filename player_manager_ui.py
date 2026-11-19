#!/usr/bin/env python
"""
Interactive user interface for managing baseball players
"""

import sys

# Define the classes needed
class Player(object):
    """
    Creates a MLB player
    """
    def __init__(self,firstName,lastName,throwingHand,battingHand):
        """
        battingHand='Left','Right','Switch'
        throwingHand='Left','Right'
        """
        self.name= str(firstName) + str(lastName)
        self.throwingHand=throwingHand
        self.battingHand=battingHand
    
class Pitcher(Player):
    """
    A MLB pitcher. Subclass of Player
    """
    def __init__(self,firstName,lastName,age,throwingHand,battingHand,pitcherRating):
        """
        Creates a Pitcher Instance.
        Rating=an Integer 1-99
        """
        Player.__init__(self,firstName,lastName,throwingHand,battingHand)
        self.age=age
        self.rating=pitcherRating

    def getRating(self):
        return self.rating
    
    def __str__(self):
        return "Pitcher: %s (Age: %d, Rating: %d, Throws: %s)" % (self.name, self.age, self.rating, self.throwingHand)

class Batter(Player):
    """
    A MLB batter. Subclass of Player
    """
    def __init__(self,firstName,lastName,age,throwingHand,battingHand,contact):
        """
        Creates a Batter Instance.
        Contact= An integer 1-99
        """
        Player.__init__(self,firstName,lastName,throwingHand,battingHand)
        self.age=age
        self.contact=contact

    def getRating(self):
        """
        Returns a batter's rating
        """
        return self.contact
    
    def __str__(self):
        return "Batter: %s (Age: %d, Contact: %d, Bats: %s)" % (self.name, self.age, self.contact, self.battingHand)

class PlayerManager(object):
    """
    Manages storage and retrieval of players in memory
    """
    def __init__(self):
        """
        Initializes the PlayerManager with empty player storage
        """
        self.players = {}
    
    def addPitcher(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating):
        """
        Adds a new pitcher to the player storage
        """
        pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating)
        playerKey = pitcher.name
        self.players[playerKey] = pitcher
        print("Added pitcher: %s" % playerKey)
        return pitcher
    
    def addBatter(self, firstName, lastName, age, throwingHand, battingHand, contact):
        """
        Adds a new batter to the player storage
        """
        batter = Batter(firstName, lastName, age, throwingHand, battingHand, contact)
        playerKey = batter.name
        self.players[playerKey] = batter
        print("Added batter: %s" % playerKey)
        return batter
    
    def getPlayer(self, firstName, lastName):
        """
        Retrieves a player by first and last name
        """
        playerKey = str(firstName) + str(lastName)
        return self.players.get(playerKey, None)
    
    def getAllPlayers(self):
        """
        Returns all stored players
        """
        return self.players
    
    def listPlayers(self):
        """
        Prints all stored players
        """
        if not self.players:
            print("No players stored")
            return
        print("\n" + "="*60)
        print("STORED PLAYERS")
        print("="*60)
        for playerName, player in self.players.items():
            print(str(player))
        print("="*60 + "\n")
    
    def removePlayer(self, firstName, lastName):
        """
        Removes a player from storage
        """
        playerKey = str(firstName) + str(lastName)
        if playerKey in self.players:
            del self.players[playerKey]
            print("Removed player: %s" % playerKey)
            return True
        else:
            print("Player not found: %s" % playerKey)
            return False


def display_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("BASEBALL PLAYER MANAGER")
    print("="*60)
    print("1. Add a new pitcher")
    print("2. Add a new batter")
    print("3. View all players")
    print("4. Search for a player")
    print("5. Remove a player")
    print("6. Exit")
    print("="*60)


def add_pitcher(manager):
    """Interactive function to add a pitcher"""
    print("\n--- Add New Pitcher ---")
    try:
        firstName = input("Enter first name: ").strip()
        lastName = input("Enter last name: ").strip()
        age = int(input("Enter age: "))
        
        print("Throwing hand options: Left, Right")
        throwingHand = input("Enter throwing hand: ").strip()
        if throwingHand not in ['Left', 'Right']:
            print("Invalid throwing hand. Using 'Right'.")
            throwingHand = 'Right'
        
        print("Batting hand options: Left, Right, Switch")
        battingHand = input("Enter batting hand: ").strip()
        if battingHand not in ['Left', 'Right', 'Switch']:
            print("Invalid batting hand. Using 'Right'.")
            battingHand = 'Right'
        
        rating = int(input("Enter pitcher rating (1-99): "))
        if rating < 1 or rating > 99:
            print("Rating must be between 1 and 99. Using 50.")
            rating = 50
        
        pitcher = manager.addPitcher(firstName, lastName, age, throwingHand, battingHand, rating)
        print("Successfully added: %s" % str(pitcher))
    except ValueError:
        print("Invalid input. Please enter valid values.")


def add_batter(manager):
    """Interactive function to add a batter"""
    print("\n--- Add New Batter ---")
    try:
        firstName = input("Enter first name: ").strip()
        lastName = input("Enter last name: ").strip()
        age = int(input("Enter age: "))
        
        print("Throwing hand options: Left, Right")
        throwingHand = input("Enter throwing hand: ").strip()
        if throwingHand not in ['Left', 'Right']:
            print("Invalid throwing hand. Using 'Right'.")
            throwingHand = 'Right'
        
        print("Batting hand options: Left, Right, Switch")
        battingHand = input("Enter batting hand: ").strip()
        if battingHand not in ['Left', 'Right', 'Switch']:
            print("Invalid batting hand. Using 'Right'.")
            battingHand = 'Right'
        
        contact = int(input("Enter contact rating (1-99): "))
        if contact < 1 or contact > 99:
            print("Contact rating must be between 1 and 99. Using 50.")
            contact = 50
        
        batter = manager.addBatter(firstName, lastName, age, throwingHand, battingHand, contact)
        print("Successfully added: %s" % str(batter))
    except ValueError:
        print("Invalid input. Please enter valid values.")


def search_player(manager):
    """Interactive function to search for a player"""
    print("\n--- Search for Player ---")
    firstName = input("Enter first name: ").strip()
    lastName = input("Enter last name: ").strip()
    
    player = manager.getPlayer(firstName, lastName)
    if player:
        print("Found: %s" % str(player))
    else:
        print("Player not found.")


def remove_player(manager):
    """Interactive function to remove a player"""
    print("\n--- Remove Player ---")
    firstName = input("Enter first name: ").strip()
    lastName = input("Enter last name: ").strip()
    
    manager.removePlayer(firstName, lastName)


def main():
    """Main function to run the interactive interface"""
    manager = PlayerManager()
    
    print("\n" + "="*60)
    print("Welcome to the Baseball Player Manager!")
    print("="*60)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_pitcher(manager)
        elif choice == '2':
            add_batter(manager)
        elif choice == '3':
            manager.listPlayers()
        elif choice == '4':
            search_player(manager)
        elif choice == '5':
            remove_player(manager)
        elif choice == '6':
            print("\nThank you for using Baseball Player Manager!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
