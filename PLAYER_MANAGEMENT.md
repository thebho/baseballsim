# Baseball Simulator - Player Management

This document describes the player management features in the baseball simulator.

## Overview

The baseball simulator includes a `PlayerManager` class that allows users to create, store, retrieve, and manage baseball players in memory. Players can be either pitchers or batters, each with comprehensive attributes including birth date and multiple positions.

## Features

### 1. PlayerManager Class

The `PlayerManager` class provides a centralized way to manage all players in the simulation.

#### Methods

##### `addPitcher(firstName, lastName, birthDate, throwingHand, battingHand, pitcherRating, jerseyNumber=0, positions=None, team="", status="Active")`
Adds a new pitcher to the player storage.

**Parameters:**
- `firstName` (str): Pitcher's first name
- `lastName` (str): Pitcher's last name
- `birthDate` (str or datetime): Pitcher's birth date in YYYY-MM-DD format or datetime object
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `pitcherRating` (int): Rating from 1-99
- `jerseyNumber` (int, optional): Jersey number (default: 0)
- `positions` (list, optional): Additional positions beyond Pitcher (default: None, which becomes ['Pitcher'])
- `team` (str, optional): Team name (default: "")
- `status` (str, optional): 'Active' or 'Injured' (default: "Active")

**Returns:** The created Pitcher object

**Example:**
```python
manager = PlayerManager()
kershaw = manager.addPitcher('Clayton', 'Kershaw', '1987-03-19', 'Left', 'Right', 95,
                            jerseyNumber=22, positions=['DH'], 
                            team='Los Angeles Dodgers', status='Active')
```

##### `addBatter(firstName, lastName, birthDate, throwingHand, battingHand, contact, jerseyNumber=0, positions=None, team="", status="Active")`
Adds a new batter to the player storage.

**Parameters:**
- `firstName` (str): Batter's first name
- `lastName` (str): Batter's last name
- `birthDate` (str or datetime): Batter's birth date in YYYY-MM-DD format or datetime object
- `throwingHand` (str): 'Left' or 'Right'
- `battingHand` (str): 'Left', 'Right', or 'Switch'
- `contact` (int): Contact rating from 1-99
- `jerseyNumber` (int, optional): Jersey number (default: 0)
- `positions` (list, optional): Player positions, e.g., ['Catcher'], ['Outfield', 'DH'] (default: None, which becomes [])
- `team` (str, optional): Team name (default: "")
- `status` (str, optional): 'Active' or 'Injured' (default: "Active")

**Returns:** The created Batter object

**Example:**
```python
trout = manager.addBatter('Mike', 'Trout', '1991-08-07', 'Right', 'Right', 92,
                         jerseyNumber=27, positions=['Outfield', 'DH'], 
                         team='Los Angeles Angels', status='Active')
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
    print("Age:", player.getAge())
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
====================================================================================================
STORED PLAYERS
====================================================================================================
Pitcher: ClaytonKershaw #22 (DOB: 1987-03-19, Age: 36, Rating: 95, Throws: Left, Positions: Pitcher, DH, Team: Los Angeles Dodgers, Status: Active)
Batter: MikeTrout #27 (DOB: 1991-08-07, Age: 32, Contact: 92, Bats: Right, Positions: Outfield, DH, Team: Los Angeles Angels, Status: Active)
====================================================================================================
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

## Player Attributes and Methods

### Player Base Class

#### Attributes
- `name`: Full name (firstName + lastName)
- `firstName`: First name
- `lastName`: Last name
- `birthDate`: Birth date (datetime object)
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'
- `jerseyNumber`: Jersey number
- `positions`: List of positions (e.g., ['Pitcher'], ['Catcher', 'DH'])
- `team`: Team name
- `status`: 'Active' or 'Injured'

#### Methods
- `getAge()`: Returns calculated age based on birth date
- `addPosition(position)`: Adds a position to the player's positions list
- `removePosition(position)`: Removes a position from the player's positions list

### Pitcher (extends Player)
- `rating`: Pitcher skill rating (1-99)
- `energy`: Current energy level (0-100)
- `getRating()`: Returns pitcher rating

### Batter (extends Player)
- `contact`: Contact rating (1-99)
- `getRating()`: Returns contact rating

## Usage Examples

### Basic Usage

```python
from player_manager_ui import PlayerManager, Pitcher, Batter

# Create a player manager
manager = PlayerManager()

# Add some players with full details
kershaw = manager.addPitcher('Clayton', 'Kershaw', '1987-03-19', 'Left', 'Right', 95,
                            jerseyNumber=22, positions=['DH'],
                            team='Los Angeles Dodgers')
trout = manager.addBatter('Mike', 'Trout', '1991-08-07', 'Right', 'Right', 92,
                         jerseyNumber=27, positions=['Outfield', 'DH'],
                         team='Los Angeles Angels')

# List all players
manager.listPlayers()

# Search for a player
player = manager.getPlayer('Clayton', 'Kershaw')
if player:
    print("Found:", player.name)
    print("Age:", player.getAge())
    print("Positions:", player.positions)
    print("Team:", player.team)
    print("Status:", player.status)

# Add additional position to a player
player.addPosition('Outfield')

# Remove a player
manager.removePlayer('Mike', 'Trout')
```

### Interactive Interface

For an interactive user interface, run the `player_manager_ui.py` script:

```bash
python player_manager_ui.py
```

This will launch an interactive menu where you can:
1. Add a new pitcher (with all details including birth date and positions)
2. Add a new batter (with all details including birth date and positions)
3. View all players
4. Search for a player
5. Remove a player
6. Exit

## Birth Date and Age Calculation

Players are now stored with a birth date instead of age. The age is calculated dynamically based on the current date:

```python
player = manager.getPlayer('Clayton', 'Kershaw')
print("Birth date:", player.birthDate.strftime('%Y-%m-%d'))
print("Current age:", player.getAge())
```

Birth dates must be provided in YYYY-MM-DD format (e.g., '1987-03-19').

## Multiple Positions

Players can now have multiple positions:

- **Pitchers** always have 'Pitcher' as their first position, with optional additional positions (e.g., DH, Outfield)
- **Batters** can have any positions (e.g., Catcher, Outfield, Infield, DH)

```python
# Pitcher with multiple positions
ohtani = manager.addPitcher('Shohei', 'Ohtani', '1994-07-05', 'Left', 'Left', 96,
                           jerseyNumber=17, positions=['DH', 'Outfield'],
                           team='Los Angeles Dodgers')
print(ohtani.positions)  # ['Pitcher', 'DH', 'Outfield']

# Batter with multiple positions
trout = manager.addBatter('Mike', 'Trout', '1991-08-07', 'Right', 'Right', 92,
                         jerseyNumber=27, positions=['Outfield', 'DH'],
                         team='Los Angeles Angels')
print(trout.positions)  # ['Outfield', 'DH']

# Add position dynamically
trout.addPosition('Infield')
print(trout.positions)  # ['Outfield', 'DH', 'Infield']
```

## Files

- `atbat.py`: Main simulation file with PlayerManager class and enhanced Player/Pitcher/Batter classes
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
- Team management and roster organization
- Game simulation with stored players
- Player performance history and trends
- Player injury tracking and recovery
