#!/usr/bin/env python
"""
Test script for the interactive player manager interface
"""

import sys
from io import StringIO

# Import the player manager UI module
exec(open('player_manager_ui.py').read().split('if __name__ == "__main__":')[0])

# Test the PlayerManager class
print("="*60)
print("TESTING PLAYER MANAGER INTERFACE")
print("="*60)

manager = PlayerManager()

# Test adding pitchers with birth date and positions
print("\n--- Test 1: Adding Pitchers with Birth Date and Positions ---")
p1 = manager.addPitcher('Clayton', 'Kershaw', '1987-03-19', 'Left', 'Right', 95, 
                       jerseyNumber=22, positions=['DH'])
print(str(p1))

p2 = manager.addPitcher('Max', 'Scherzer', '1984-07-27', 'Right', 'Right', 94,
                       jerseyNumber=31)
print(str(p2))

# Test adding batters with birth date and positions
print("\n--- Test 2: Adding Batters with Birth Date and Positions ---")
b1 = manager.addBatter('Mike', 'Trout', '1991-08-07', 'Right', 'Right', 92,
                      jerseyNumber=27, positions=['Outfield', 'DH'])
print(str(b1))

b2 = manager.addBatter('Mookie', 'Betts', '1992-10-07', 'Right', 'Right', 90,
                      jerseyNumber=50, positions=['Outfield'])
print(str(b2))

# Test listing players
print("\n--- Test 3: Listing All Players ---")
manager.listPlayers()

# Test searching for a player
print("--- Test 4: Searching for Players ---")
found = manager.getPlayer('Clayton', 'Kershaw')
if found:
    print("Found: %s" % str(found))
    print("Age: %d" % found.getAge())

not_found = manager.getPlayer('John', 'Doe')
if not_found:
    print("Found: %s" % str(not_found))
else:
    print("Player 'JohnDoe' not found (as expected)")

# Test adding positions to a player
print("\n--- Test 5: Adding Positions to a Player ---")
b1.addPosition('Infield')
print("Trout positions after adding Infield: %s" % b1.positions)

# Test removing positions from a player
print("\n--- Test 6: Removing Positions from a Player ---")
b1.removePosition('DH')
print("Trout positions after removing DH: %s" % b1.positions)

# Test removing a player
print("\n--- Test 7: Removing a Player ---")
manager.removePlayer('Mookie', 'Betts')
print("After removal:")
manager.listPlayers()

# Test removing non-existent player
print("--- Test 8: Removing Non-existent Player ---")
manager.removePlayer('Non', 'Existent')

print("\n" + "="*60)
print("ALL TESTS COMPLETED SUCCESSFULLY")
print("="*60)
