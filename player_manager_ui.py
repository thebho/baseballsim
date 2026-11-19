#!/usr/bin/env python
"""
Interactive user interface for managing baseball players
"""

import sys
from datetime import datetime

# Define the classes needed
class Player(object):
    """
    Creates a MLB player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, birthDate, jerseyNumber=0, positions=None, team="", status="Active"):
        """
        battingHand='Left','Right','Switch'
        throwingHand='Left','Right'
        birthDate: Player's birth date (YYYY-MM-DD format or datetime object)
        positions: List of positions (e.g., ['Pitcher'], ['Catcher', 'DH'])
        team: Team name
        status: 'Active' or 'Injured'
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
    
    def __str__(self):
        positions_str = ", ".join(self.positions) if self.positions else "None"
        return "Pitcher: %s #%d (DOB: %s, Age: %d, Rating: %d, Throws: %s, Positions: %s, Team: %s, Status: %s)" % (
            self.name, self.jerseyNumber, self.birthDate.strftime('%Y-%m-%d'), self.getAge(), self.rating, 
            self.throwingHand, positions_str, self.team, self.status)

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
    
    def __str__(self):
        positions_str = ", ".join(self.positions) if self.positions else "None"
        return "Batter: %s #%d (DOB: %s, Age: %d, Contact: %d, Bats: %s, Positions: %s, Team: %s, Status: %s)" % (
            self.name, self.jerseyNumber, self.birthDate.strftime('%Y-%m-%d'), self.getAge(), self.contact, 
            self.battingHand, positions_str, self.team, self.status)

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
        print("\n" + "="*100)
        print("STORED PLAYERS")
        print("="*100)
        for playerName, player in self.players.items():
            print(str(player))
        print("="*100 + "\n")
    
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


def parse_positions(position_input):
    """Parse comma-separated positions into a list"""
    if not position_input.strip():
        return []
    return [pos.strip() for pos in position_input.split(',')]


def add_pitcher(manager):
    """Interactive function to add a pitcher"""
    print("\n--- Add New Pitcher ---")
    try:
        firstName = input("Enter first name: ").strip()
        lastName = input("Enter last name: ").strip()
        
        birthDate = input("Enter birth date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(birthDate, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using 1990-01-01.")
            birthDate = '1990-01-01'
        
        jerseyNumber = int(input("Enter jersey number: "))
        
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
        
        print("Enter additional positions (comma-separated, e.g., 'DH, Outfield'):")
        print("(Pitcher is added by default)")
        positions_input = input("Additional positions: ").strip()
        positions = parse_positions(positions_input)
        
        team = input("Enter team name: ").strip()
        
        print("Status options: Active, Injured")
        status = input("Enter status (default: Active): ").strip()
        if status not in ['Active', 'Injured']:
            status = 'Active'
        
        rating = int(input("Enter pitcher rating (1-99): "))
        if rating < 1 or rating > 99:
            print("Rating must be between 1 and 99. Using 50.")
            rating = 50
        
        pitcher = manager.addPitcher(firstName, lastName, birthDate, throwingHand, battingHand, rating, 
                                    jerseyNumber, positions, team, status)
        print("Successfully added: %s" % str(pitcher))
    except ValueError:
        print("Invalid input. Please enter valid values.")


def add_batter(manager):
    """Interactive function to add a batter"""
    print("\n--- Add New Batter ---")
    try:
        firstName = input("Enter first name: ").strip()
        lastName = input("Enter last name: ").strip()
        
        birthDate = input("Enter birth date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(birthDate, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Using 1990-01-01.")
            birthDate = '1990-01-01'
        
        jerseyNumber = int(input("Enter jersey number: "))
        
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
        
        print("Enter positions (comma-separated, e.g., 'Catcher, DH'):")
        positions_input = input("Positions: ").strip()
        positions = parse_positions(positions_input)
        
        team = input("Enter team name: ").strip()
        
        print("Status options: Active, Injured")
        status = input("Enter status (default: Active): ").strip()
        if status not in ['Active', 'Injured']:
            status = 'Active'
        
        contact = int(input("Enter contact rating (1-99): "))
        if contact < 1 or contact > 99:
            print("Contact rating must be between 1 and 99. Using 50.")
            contact = 50
        
        batter = manager.addBatter(firstName, lastName, birthDate, throwingHand, battingHand, contact, 
                                  jerseyNumber, positions, team, status)
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
