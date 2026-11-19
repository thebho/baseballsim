# Baseball Simulator - Player Management

This document describes the new player management features added to the baseball simulator.

## Overview

The baseball simulator now includes a `PlayerManager` class that allows users to create, store, retrieve, and manage baseball players in memory. Players can be either pitchers or batters, each with their own attributes and ratings.

## Features

### 1. PlayerManager Class

The `PlayerManager` class provides a centralized way to manage all players in the simulation.

#### Methods

##### `addPitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating)`
Adds a new pitcher to the player storage.

**Parameters:**
- `firstName` (str): Pitcher's first name
- `lastName` (str): Pitcher's last name
- `age` (int): Pitcher's age
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `pitcherRating` (int): Rating from 1-99

**Returns:** The created Pitcher object

**Example:**
```python
manager = PlayerManager()
kershaw = manager.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95)
```

##### `addBatter(firstName, lastName, age, throwingHand, battingHand, contact)`
Adds a new batter to the player storage.

**Parameters:**
- `firstName` (str): Batter's first name
- `lastName` (str): Batter's last name
- `age` (int): Batter's age
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `contact` (int): Contact rating from 1-99

**Returns:** The created Batter object

**Example:**
```python
trout = manager.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92)
```

##### `getPlayer(firstName, lastName)`
Retrieves a player by first and last name.

**Parameters:**
- `firstName` (str): Player's first name
- `lastName` (str): Player's last name

**Returns:** The Player object if found, None otherwise

**Example:**
```python
player = manager.getPlayer('Clayton', 'Kershaw')
if player:
    print("Found:", player.name)
```

##### `getAllPlayers()`
Returns all stored players.

**Returns:** Dictionary of all players (key: player name, value: Player object)

**Example:**
```python
all_players = manager.getAllPlayers()
print("Total players:", len(all_players))
```

##### `listPlayers()`
Prints all stored players in a formatted list.

**Example:**
```python
manager.listPlayers()
```

Output:
```
============================================================
STORED PLAYERS
============================================================
Pitcher: ClaytonKershaw (Age: 30, Rating: 95, Throws: Left)
Batter: MikeTrout (Age: 28, Contact: 92, Bats: Right)
============================================================
```

##### `removePlayer(firstName, lastName)`
Removes a player from storage.

**Parameters:**
- `firstName` (str): Player's first name
- `lastName` (str): Player's last name

**Returns:** True if player was removed, False if not found

**Example:**
```python
success = manager.removePlayer('Mike', 'Trout')
```

## Usage Examples

### Basic Usage

```python
from atbat import PlayerManager, Pitcher, Batter

# Create a player manager
manager = PlayerManager()

# Add some players
kershaw = manager.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95)
trout = manager.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92)

# List all players
manager.listPlayers()

# Search for a player
player = manager.getPlayer('Clayton', 'Kershaw')
if player:
    print("Found:", player.name, "Rating:", player.getRating())

# Remove a player
manager.removePlayer('Mike', 'Trout')
```

### Interactive Interface

For an interactive user interface, run the `player_manager_ui.py` script:

```bash
python player_manager_ui.py
```

This will launch an interactive menu where you can:
1. Add a new pitcher
2. Add a new batter
3. View all players
4. Search for a player
5. Remove a player
6. Exit

## Player Attributes

### Pitcher
- `name`: Full name (firstName + lastName)
- `age`: Age in years
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'
- `rating`: Pitcher skill rating (1-99)
- `energy`: Current energy level (0-100)

### Batter
- `name`: Full name (firstName + lastName)
- `age`: Age in years
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'
- `contact`: Contact rating (1-99)

## Files

- `atbat.py`: Main simulation file with PlayerManager class
- `player_manager_ui.py`: Interactive user interface for player management
- `test_player_manager.py`: Unit tests for PlayerManager class
- `test_ui.py`: Tests for the interactive interface

## Testing

Run the test scripts to verify functionality:

```bash
# Test the PlayerManager class
python test_player_manager.py

# Test the interactive interface
python test_ui.py
```

## Future Enhancements

Potential improvements for future versions:
- Persistent storage (save/load players to/from file)
- Player statistics tracking
- Team management
- Game simulation with stored players
- Player performance history
