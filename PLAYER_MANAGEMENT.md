# Baseball Simulator - Player Management

This document describes the player management features in the baseball simulator.

## Overview

The baseball simulator includes a `PlayerManager` class that allows users to create, store, retrieve, and manage baseball players in memory. Players can be either pitchers or batters, each with comprehensive attributes and statistics.

## Features

### 1. PlayerManager Class

The `PlayerManager` class provides a centralized way to manage all players in the simulation.

#### Methods

##### `addPitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating, jerseyNumber=0, team="", status="Active", wins=0, losses=0, era=0.0, strikeouts=0)`
Adds a new pitcher to the player storage.

**Parameters:**
- `firstName` (str): Pitcher's first name
- `lastName` (str): Pitcher's last name
- `age` (int): Pitcher's age
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `pitcherRating` (int): Rating from 1-99
- `jerseyNumber` (int, optional): Jersey number (default: 0)
- `team` (str, optional): Team name (default: "")
- `status` (str, optional): 'Active' or 'Injured' (default: "Active")
- `wins` (int, optional): Career wins (default: 0)
- `losses` (int, optional): Career losses (default: 0)
- `era` (float, optional): Earned Run Average (default: 0.0)
- `strikeouts` (int, optional): Career strikeouts (default: 0)

**Returns:** The created Pitcher object

**Example:**
```python
manager = PlayerManager()
kershaw = manager.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95,
                            jerseyNumber=22, team='Los Angeles Dodgers', 
                            status='Active', wins=169, losses=74, 
                            era=2.48, strikeouts=2396)
```

##### `addBatter(firstName, lastName, age, throwingHand, battingHand, contact, jerseyNumber=0, position="", team="", status="Active", hits=0, strikeouts=0)`
Adds a new batter to the player storage.

**Parameters:**
- `firstName` (str): Batter's first name
- `lastName` (str): Batter's last name
- `age` (int): Batter's age
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `contact` (int): Contact rating from 1-99
- `jerseyNumber` (int, optional): Jersey number (default: 0)
- `position` (str, optional): Player position, e.g., 'Catcher', 'Outfield', 'Infield' (default: "")
- `team` (str, optional): Team name (default: "")
- `status` (str, optional): 'Active' or 'Injured' (default: "Active")
- `hits` (int, optional): Career hits (default: 0)
- `strikeouts` (int, optional): Career strikeouts (default: 0)

**Returns:** The created Batter object

**Example:**
```python
trout = manager.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92,
                         jerseyNumber=27, position='Outfield', 
                         team='Los Angeles Angels', status='Active',
                         hits=1949, strikeouts=1337)
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
================================================================================
STORED PLAYERS
================================================================================
Pitcher: ClaytonKershaw #22 (Age: 30, Rating: 95, Throws: Left, Team: Los Angeles Dodgers, Status: Active, W-L: 169-74, ERA: 2.48, K: 2396)
Batter: MikeTrout #27 (Age: 28, Contact: 92, Bats: Right, Position: Outfield, Team: Los Angeles Angels, Status: Active, Hits: 1949, K: 1337)
================================================================================
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

# Add some players with full details
kershaw = manager.addPitcher('Clayton', 'Kershaw', 30, 'Left', 'Right', 95,
                            jerseyNumber=22, team='Los Angeles Dodgers',
                            wins=169, losses=74, era=2.48, strikeouts=2396)
trout = manager.addBatter('Mike', 'Trout', 28, 'Right', 'Right', 92,
                         jerseyNumber=27, position='Outfield',
                         team='Los Angeles Angels', hits=1949, strikeouts=1337)

# List all players
manager.listPlayers()

# Search for a player
player = manager.getPlayer('Clayton', 'Kershaw')
if player:
    print("Found:", player.name, "Rating:", player.getRating())
    print("Team:", player.team)
    print("Status:", player.status)

# Remove a player
manager.removePlayer('Mike', 'Trout')
```

### Interactive Interface

For an interactive user interface, run the `player_manager_ui.py` script:

```bash
python player_manager_ui.py
```

This will launch an interactive menu where you can:
1. Add a new pitcher (with all details)
2. Add a new batter (with all details)
3. View all players
4. Search for a player
5. Remove a player
6. Exit

## Player Attributes

### Pitcher
- `name`: Full name (firstName + lastName)
- `firstName`: First name
- `lastName`: Last name
- `age`: Age in years
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'
- `jerseyNumber`: Jersey number
- `position`: Always 'Pitcher'
- `team`: Team name
- `status`: 'Active' or 'Injured'
- `rating`: Pitcher skill rating (1-99)
- `energy`: Current energy level (0-100)
- `wins`: Career wins
- `losses`: Career losses
- `era`: Earned Run Average
- `strikeouts`: Career strikeouts

### Batter
- `name`: Full name (firstName + lastName)
- `firstName`: First name
- `lastName`: Last name
- `age`: Age in years
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'
- `jerseyNumber`: Jersey number
- `position`: Player position (e.g., 'Catcher', 'Outfield', 'Infield')
- `team`: Team name
- `status`: 'Active' or 'Injured'
- `contact`: Contact rating (1-99)
- `hits`: Career hits
- `strikeouts`: Career strikeouts

## Files

- `atbat.py`: Main simulation file with PlayerManager class and enhanced Player/Pitcher/Batter classes
- `player_manager_ui.py`: Interactive user interface for player management
- `test_player_manager.py`: Unit tests for PlayerManager class with enhanced player details
- `test_ui.py`: Tests for the interactive interface

## Testing

Run the test scripts to verify functionality:

```bash
# Test the PlayerManager class with enhanced details
python test_player_manager.py

# Test the interactive interface
python test_ui.py
```

## Future Enhancements

Potential improvements for future versions:
- Persistent storage (save/load players to/from file)
- Advanced player statistics tracking
- Team management and roster organization
- Game simulation with stored players
- Player performance history and trends
- Player injury tracking and recovery
