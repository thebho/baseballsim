#!/usr/bin/env python
"""Test script for PlayerManager functionality with birth date and multiple positions"""

# Test the PlayerManager class without importing the full module
import sys
sys.path.insert(0, '/workspace')

from datetime import datetime

# Define the classes needed for testing
class Player(object):
    """
    Creates a MLB player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, birthDate, jerseyNumber=0, positions=None, team="", status="Active"):
        """
        birthDate: Player's birth date (YYYY-MM-DD format or datetime object)
        positions: List of positions (e.g., ['Pitcher'], ['Catcher', 'DH'])
        """
        self.name = str(firstName) + str(lastName)
        self.firstName = firstName
        self.lastName = lastName
        self.throwingHand = throwingHand
        self.battingHand = battingHand
        self.birthDate = self._parse_date(birthDate)
        self.jerseyNumber = jerseyNumber
        self.positions = positions if positions else []
        self.team = team
        self.status = status
    
    def _parse_date(self, date_input):
        """Parse date from string or datetime object"""
        if isinstance(date_input, datetime):
            return date_input
        elif isinstance(date_input, str):
            try:
                return datetime.strptime(date_input, '%Y-%m-%d')
            except ValueError:
                raise ValueError("Date must be in YYYY-MM-DD format")
        else:
            raise ValueError("Date must be a string (YYYY-MM-DD) or datetime object")
    
    def getAge(self):
        """Calculate age from birth date"""
        today = datetime.now()
        age = today.year - self.birthDate.year
        if (today.month, today.day) < (self.birthDate.month, self.birthDate.day):
            age -= 1
        return age
    
    def addPosition(self, position):
        """Add a position to the player's positions list"""
        if position not in self.positions:
            self.positions.append(position)
    
    def removePosition(self, position):
        """Remove a position from the player's positions list"""
        if position in self.positions:
            self.positions.remove(position)
    
class Pitcher(Player):
    """
    A MLB pitcher. Subclass of Player
    """
    def __init__(self, firstName, lastName, birthDate, throwingHand, battingHand, pitcherRating,
                 jerseyNumber=0, positions=None, team="", status="Active"):
        """
        Creates a Pitcher Instance.
        Rating=an Integer 1-99
        positions: List of positions (defaults to ['Pitcher'])
        """
        if positions is None:
            positions = ['Pitcher']
        elif 'Pitcher' not in positions:
            positions = ['Pitcher'] + positions
        
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, birthDate, jerseyNumber, positions, team, status)
        self.rating = pitcherRating

    def getRating(self):
        return self.rating

class Batter(Player):
    """
    A MLB batter. Subclass of Player
    """
    def __init__(self, firstName, lastName, birthDate, throwingHand, battingHand, contact,
                 jerseyNumber=0, positions=None, team="", status="Active"):
        """
        Creates a Batter Instance.
        Contact= An integer 1-99
        positions: List of positions (e.g., ['Catcher'], ['Outfield', 'DH'])
        """
        if positions is None:
            positions = []
        
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, birthDate, jerseyNumber, positions, team, status)
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
    
    def addPitcher(self, firstName, lastName, birthDate, throwingHand, battingHand, pitcherRating,
                   jerseyNumber=0, positions=None, team="", status="Active"):
        """
        Adds a new pitcher to the player storage
        """
        pitcher = Pitcher(firstName, lastName, birthDate, throwingHand, battingHand, pitcherRating,
                         jerseyNumber, positions, team, status)
        playerKey = pitcher.name
        self.players[playerKey] = pitcher
        print("Added pitcher: %s" % playerKey)
        return pitcher
    
    def addBatter(self, firstName, lastName, birthDate, throwingHand, battingHand, contact,
                  jerseyNumber=0, positions=None, team="", status="Active"):
        """
        Adds a new batter to the player storage
        """
        batter = Batter(firstName, lastName, birthDate, throwingHand, battingHand, contact,
                       jerseyNumber, positions, team, status)
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
            positions_str = ", ".join(player.positions) if player.positions else "None"
            print("  - %s (%s) - Positions: %s, Age: %d" % (playerName, playerType, positions_str, player.getAge()))
    
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

# Test adding pitchers with birth date and positions
print("=== Testing Add Pitcher with Birth Date and Positions ===")
kershaw = pm.addPitcher('Clayton', 'Kershaw', '1987-03-19', 'Left', 'Right', 95, 
                        jerseyNumber=22, positions=['DH'], team='Los Angeles Dodgers', status='Active')
print("Pitcher rating:", kershaw.getRating())
print("Birth date:", kershaw.birthDate.strftime('%Y-%m-%d'))
print("Age:", kershaw.getAge())
print("Positions:", kershaw.positions)
print("Jersey number:", kershaw.jerseyNumber)
print("Team:", kershaw.team)
print("Status:", kershaw.status)

# Test adding batters with birth date and positions
print("\n=== Testing Add Batter with Birth Date and Positions ===")
trout = pm.addBatter('Mike', 'Trout', '1991-08-07', 'Right', 'Right', 92,
                     jerseyNumber=27, positions=['Outfield', 'DH'], team='Los Angeles Angels', status='Active')
print("Batter rating:", trout.getRating())
print("Birth date:", trout.birthDate.strftime('%Y-%m-%d'))
print("Age:", trout.getAge())
print("Positions:", trout.positions)
print("Jersey number:", trout.jerseyNumber)
print("Team:", trout.team)
print("Status:", trout.status)

# Test adding injured player
print("\n=== Testing Add Injured Player ===")
injured_pitcher = pm.addPitcher('Max', 'Scherzer', '1984-07-27', 'Right', 'Right', 94,
                               jerseyNumber=31, team='New York Mets', status='Injured')
print("Status:", injured_pitcher.status)
print("Age:", injured_pitcher.getAge())

# Test adding position to player
print("\n=== Testing Add Position to Player ===")
kershaw.addPosition('Outfield')
print("Kershaw positions after adding Outfield:", kershaw.positions)

# Test removing position from player
print("\n=== Testing Remove Position from Player ===")
kershaw.removePosition('DH')
print("Kershaw positions after removing DH:", kershaw.positions)

# Test listing players
print("\n=== Testing List Players ===")
pm.listPlayers()

# Test retrieving a player
print("\n=== Testing Get Player ===")
retrieved_pitcher = pm.getPlayer('Clayton', 'Kershaw')
if retrieved_pitcher:
    print("Retrieved pitcher:", retrieved_pitcher.name)
    print("Birth date:", retrieved_pitcher.birthDate.strftime('%Y-%m-%d'))
    print("Age:", retrieved_pitcher.getAge())
    print("Positions:", retrieved_pitcher.positions)
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
default_pitcher = pm.addPitcher('John', 'Doe', '1995-06-15', 'Right', 'Right', 75)
print("Default jersey number:", default_pitcher.jerseyNumber)
print("Default team:", default_pitcher.team)
print("Default status:", default_pitcher.status)
print("Default positions:", default_pitcher.positions)
print("Age:", default_pitcher.getAge())

# Test pitcher with multiple positions
print("\n=== Testing Pitcher with Multiple Positions ===")
multi_pitcher = pm.addPitcher('Shohei', 'Ohtani', '1994-07-05', 'Left', 'Left', 96,
                             jerseyNumber=17, positions=['DH', 'Outfield'], 
                             team='Los Angeles Dodgers', status='Active')
print("Positions:", multi_pitcher.positions)
print("Pitcher is always first:", multi_pitcher.positions[0] == 'Pitcher')

print("\n=== All Tests Complete ===")
