#!/usr/bin/env python
"""Test script for PlayerManager functionality"""

# Test the PlayerManager class without importing the full module
import sys
sys.path.insert(0, '/workspace')

# Define the classes needed for testing
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
        self.energy=100
        self.rating=pitcherRating

    def getRating(self):
        return self.rating

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
        self.contact=contact

    def getRating(self):
        """
        Returns a batter's rating
        """
        return self.contact

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
        
        Args:
            firstName: Pitcher's first name
            lastName: Pitcher's last name
            age: Pitcher's age
            throwingHand: 'Left' or 'Right'
            battingHand: 'Left', 'Right', or 'Switch'
            pitcherRating: Integer 1-99
        
        Returns:
            The created Pitcher object
        """
        pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating)
        playerKey = pitcher.name
        self.players[playerKey] = pitcher
        print("Added pitcher: %s" % playerKey)
        return pitcher
    
    def addBatter(self, firstName, lastName, age, throwingHand, battingHand, contact):
        """
        Adds a new batter to the player storage
        
        Args:
            firstName: Batter's first name
            lastName: Batter's last name
            age: Batter's age
            throwingHand: 'Left' or 'Right'
            battingHand: 'Left', 'Right', or 'Switch'
            contact: Integer 1-99
        
        Returns:
            The created Batter object
        """
        batter = Batter(firstName, lastName, age, throwingHand, battingHand, contact)
        playerKey = batter.name
        self.players[playerKey] = batter
        print("Added batter: %s" % playerKey)
        return batter
    
    def getPlayer(self, firstName, lastName):
        """
        Retrieves a player by first and last name
        
        Args:
            firstName: Player's first name
            lastName: Player's last name
        
        Returns:
            The Player object if found, None otherwise
        """
        playerKey = str(firstName) + str(lastName)
        return self.players.get(playerKey, None)
    
    def getAllPlayers(self):
        """
        Returns all stored players
        
        Returns:
            Dictionary of all players
        """
        return self.players
    
    def listPlayers(self):
        """
        Prints all stored players
        """
        if not self.players:
            print("No players stored")
            return
        print("Stored Players:")
        for playerName, player in self.players.items():
            playerType = "Pitcher" if isinstance(player, Pitcher) else "Batter"
            print("  - %s (%s)" % (playerName, playerType))
    
    def removePlayer(self, firstName, lastName):
        """
        Removes a player from storage
        
        Args:
            firstName: Player's first name
            lastName: Player's last name
        
        Returns:
            True if player was removed, False if not found
        """
        playerKey = str(firstName) + str(lastName)
        if playerKey in self.players:
            del self.players[playerKey]
            print("Removed player: %s" % playerKey)
            return True
        else:
            print("Player not found: %s" % playerKey)
            return False


# Run tests
pm = PlayerManager()

# Test adding pitchers
print("=== Testing Add Pitcher ===")
kershaw = pm.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95)
print("Pitcher rating:", kershaw.getRating())

# Test adding batters
print("\n=== Testing Add Batter ===")
trout = pm.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92)
print("Batter rating:", trout.getRating())

# Test listing players
print("\n=== Testing List Players ===")
pm.listPlayers()

# Test retrieving a player
print("\n=== Testing Get Player ===")
retrieved_pitcher = pm.getPlayer('Clayton', 'Kershaw')
if retrieved_pitcher:
    print("Retrieved pitcher:", retrieved_pitcher.name)
else:
    print("Pitcher not found")

# Test getting all players
print("\n=== Testing Get All Players ===")
all_players = pm.getAllPlayers()
print("Total players stored:", len(all_players))

# Test removing a player
print("\n=== Testing Remove Player ===")
pm.removePlayer('Mike', 'Trout')
pm.listPlayers()

# Test removing non-existent player
print("\n=== Testing Remove Non-existent Player ===")
pm.removePlayer('Non', 'Existent')

print("\n=== All Tests Complete ===")
