# Baseball Simulator

A Python-based baseball simulation engine that models at-bat sequences between pitchers and batters.

## Overview

This project simulates realistic baseball at-bats by modeling:
- **Pitcher mechanics**: Pitch selection, location, and quality based on pitcher skill and energy
- **Batter mechanics**: Swing decisions and contact probability based on batter skill
- **Game logic**: Strike zone detection, ball/strike counting, and at-bat outcomes
- **Visualization**: Pitch location plotting with strike zone overlay

## Features

- **Player Classes**: Pitcher and Batter objects with customizable attributes
- **Pitch Simulation**: Realistic pitch selection from a pitcher's repertoire with location variance
- **Swing Logic**: Intelligent swing/take decisions based on count and pitch location
- **Contact Mechanics**: Contact probability influenced by pitcher-batter skill matchup
- **Visual Output**: Matplotlib visualization of pitch locations during an at-bat

## Project Structure

```
baseballsim/
├── atbat.py          # Main simulation engine
├── README.md         # This file
└── .gitignore        # Git ignore rules
```

## Usage

### Basic Example

```python
from atbat import Pitcher, Batter, atBat

# Create a pitcher (name, age, throwing hand, batting hand, rating 1-99)
pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)

# Create a batter (name, age, throwing hand, batting hand, contact rating 1-99)
batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Simulate an at-bat
atBat(pitcher, batter)
```

### Classes

#### Player
Base class for all players with name, throwing hand, and batting hand.

#### Pitcher(Player)
- **Parameters**: firstName, lastName, age, throwingHand, battingHand, pitcherRating
- **Attributes**: 
  - `rating`: Pitcher skill (1-99)
  - `energy`: Current energy level (0-100)
  - `pitchDict`: Available pitches

#### Batter(Player)
- **Parameters**: firstName, lastName, age, throwingHand, battingHand, contact
- **Attributes**:
  - `contact`: Batter skill (1-99)

#### Pitch
Represents a single pitch with location, type, and quality.

#### Swing
Handles swing/take decisions and contact probability.

## Game Mechanics

### Strike Zone
- **Width**: -0.85 to 0.85 (horizontal)
- **Height**: -2.0 to 1.5 (vertical)

### At-Bat Logic
1. Pitcher throws a pitch with random location and type
2. Batter decides to swing or take based on count and pitch location
3. If swing: determine if contact is made
4. Continue until 4 balls (walk), 3 strikes (strikeout), or ball in play

### Pitch Quality
Influenced by pitcher rating and energy, affecting contact probability.

## Dependencies

- Python 2.7+
- matplotlib (pylab)

## Output

The simulation generates:
- Console output of pitch-by-pitch action
- Matplotlib visualization showing:
  - All pitch locations
  - Strike zone boundaries
  - Pitch labels for reference

## Future Enhancements

- Ball in play outcome simulation (hits, outs, etc.)
- Multiple pitch types with different characteristics
- Pitcher fatigue mechanics
- Batter hot/cold streaks
- Full game simulation
- Advanced statistics tracking

## License

This project is open source and available for educational purposes.
