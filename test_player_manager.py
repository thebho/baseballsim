#!/usr/bin/env python
"""Test script for PlayerManager functionality with enhanced player details"""

# Test the PlayerManager class without importing the full module
import sys
sys.path.insert(0, '/workspace')

# Define the classes needed for testing
class Player(object):
    """
    Creates a MLB player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber=0, position="", team="", status="Active"):
        """
        battingHand='Left','Right','Switch'
        throwingHand='Left','Right'
        position: Player's position (e.g., 'Pitcher', 'Catcher', 'Outfield')
        team: Team name
        status: 'Active' or 'Injured'
        """
        self.name = str(firstName) + str(lastName)
        self.firstName = firstName
        self.lastName = lastName
        self.throwingHand = throwingHand
        self.battingHand = battingHand
        self.jerseyNumber = jerseyNumber
        self.position = position
        self.team = team
        self.status = status
    
class Pitcher(Player):
    """
    A MLB pitcher. Subclass of Player
    """
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                 jerseyNumber=0, team="", status="Active"):
        """
        Creates a Pitcher Instance.
        Rating=an Integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber, "Pitcher", team, status)
        self.age = age
        self.rating = pitcherRating

    def getRating(self):
        return self.rating

class Batter(Player):
    """
    A MLB batter. Subclass of Player
    """
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, contact,
                 jerseyNumber=0, position="", team="", status="Active"):
        """
        Creates a Batter Instance.
        Contact= An integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber, position, team, status)
        self.age = age
        self.contact = contact

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
    
    def addPitcher(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                   jerseyNumber=0, team="", status="Active"):
        """
        Adds a new pitcher to the player storage
        """
        pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                         jerseyNumber, team, status)
        playerKey = pitcher.name
        self.players[playerKey] = pitcher
        print("Added pitcher: %s" % playerKey)
        return pitcher
    
    def addBatter(self, firstName, lastName, age, throwingHand, battingHand, contact,
                  jerseyNumber=0, position="", team="", status="Active"):
        """
        Adds a new batter to the player storage
        """
        batter = Batter(firstName, lastName, age, throwingHand, battingHand, contact,
                       jerseyNumber, position, team, status)
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
        print("Stored Players:")
        for playerName, player in self.players.items():
            playerType = "Pitcher" if isinstance(player, Pitcher) else "Batter"
            print("  - %s (%s)" % (playerName, playerType))
    
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


# Run tests
pm = PlayerManager()

# Test adding pitchers with new fields
print("=== Testing Add Pitcher with Enhanced Details ===")
kershaw = pm.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95, 
                        jerseyNumber=22, team='Los Angeles Dodgers', status='Active')
print("Pitcher rating:", kershaw.getRating())
print("Jersey number:", kershaw.jerseyNumber)
print("Team:", kershaw.team)
print("Status:", kershaw.status)

# Test adding batters with new fields
print("\n=== Testing Add Batter with Enhanced Details ===")
trout = pm.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92,
                     jerseyNumber=27, position='Outfield', team='Los Angeles Angels', status='Active')
print("Batter rating:", trout.getRating())
print("Jersey number:", trout.jerseyNumber)
print("Position:", trout.position)
print("Team:", trout.team)
print("Status:", trout.status)

# Test adding injured player
print("\n=== Testing Add Injured Player ===")
injured_pitcher = pm.addPitcher('Max', 'Scherzer', 35, 'Right', 'Right', 94,
                               jerseyNumber=31, team='New York Mets', status='Injured')
print("Status:", injured_pitcher.status)

# Test listing players
print("\n=== Testing List Players ===")
pm.listPlayers()

# Test retrieving a player
print("\n=== Testing Get Player ===")
retrieved_pitcher = pm.getPlayer('Clayton', 'Kershaw')
if retrieved_pitcher:
    print("Retrieved pitcher:", retrieved_pitcher.name)
    print("Jersey:", retrieved_pitcher.jerseyNumber)
    print("Team:", retrieved_pitcher.team)
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

# Test default values
print("\n=== Testing Default Values ===")
default_pitcher = pm.addPitcher('John', 'Doe', 25, 'Right', 'Right', 75)
print("Default jersey number:", default_pitcher.jerseyNumber)
print("Default team:", default_pitcher.team)
print("Default status:", default_pitcher.status)

print("\n=== All Tests Complete ===")
