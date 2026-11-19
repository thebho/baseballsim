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

# Test adding pitchers
print("\n--- Test 1: Adding Pitchers ---")
p1 = manager.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95)
print(str(p1))

p2 = manager.addPitcher('Max', 'Scherzer', 35, 'Right', 'Right', 94)
print(str(p2))

# Test adding batters
print("\n--- Test 2: Adding Batters ---")
b1 = manager.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92)
print(str(b1))

b2 = manager.addBatter('Mookie', 'Betts', 27, 'Right', 'Right', 90)
print(str(b2))

# Test listing players
print("\n--- Test 3: Listing All Players ---")
manager.listPlayers()

# Test searching for a player
print("--- Test 4: Searching for Players ---")
found = manager.getPlayer('Clayton', 'Kershaw')
if found:
    print("Found: %s" % str(found))

not_found = manager.getPlayer('John', 'Doe')
if not_found:
    print("Found: %s" % str(not_found))
else:
    print("Player 'JohnDoe' not found (as expected)")

# Test removing a player
print("\n--- Test 5: Removing a Player ---")
manager.removePlayer('Mookie', 'Betts')
print("After removal:")
manager.listPlayers()

# Test removing non-existent player
print("--- Test 6: Removing Non-existent Player ---")
manager.removePlayer('Non', 'Existent')

print("\n" + "="*60)
print("ALL TESTS COMPLETED SUCCESSFULLY")
print("="*60)
