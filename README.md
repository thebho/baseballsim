# Baseball At-Bat Simulator

## Project Description

BaseballSim is a Python-based baseball at-bat simulator that models realistic pitcher-batter interactions. The simulator generates complete at-bat sequences, including pitch selection, location, batter swing decisions, and contact outcomes. It provides a foundation for understanding baseball mechanics through object-oriented programming and probability-based decision making.

## Features

- **Player Creation**: Create custom Pitcher and Batter objects with realistic attributes
- **Pitch Simulation**: Generate pitches with randomized locations and quality ratings
- **Strike Zone Mechanics**: Accurate strike zone detection based on MLB standards
- **Batter Swing Logic**: Intelligent swing/take decisions based on ball-strike count
- **Contact Probability**: Contact outcomes determined by pitcher skill, batter contact rating, and pitch quality
- **Pitch Visualization**: Visual representation of pitch locations relative to the strike zone using matplotlib
- **Multiple Pitch Types**: Support for different pitch types (Fastball, ChangeUp) with distinct characteristics
- **Complete At-Bat Sequences**: Full simulation from first pitch through walk, strikeout, or ball in play

## Installation

### Requirements

- Python 2.7+ (note: code uses Python 2 print statements)
- matplotlib (for visualization)
- Standard library modules: random, math

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/thebho/baseballsim.git
   cd baseballsim
   ```

2. Ensure Python and matplotlib are installed:
   ```bash
   pip install matplotlib
   ```

## Usage

### Running the Simulator

Execute the main script to run a sample at-bat:

```bash
python atbat.py
```

This will simulate an at-bat between Bob Gibson (pitcher) and Stan Musial (batter), displaying pitch locations and the outcome.

### Creating Players

```python
from atbat import Pitcher, Batter, atBat

# Create a pitcher (name, age, throwing hand, batting hand, rating 1-99)
pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)

# Create a batter (name, age, throwing hand, batting hand, contact rating 1-99)
batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Run an at-bat
atBat(pitcher, batter)
```

## How It Works

### At-Bat Sequence

1. **Pitch Generation**: A random pitch type is selected from the pitcher's pitch dictionary
2. **Pitch Location**: A location is randomly generated within the strike zone boundaries
3. **Pitch Quality**: Quality is calculated as a value between 90-100
4. **Swing Decision**: The batter decides to swing or take based on:
   - Current ball-strike count
   - Pitch location (center, borderline, or outside)
   - Random probability factor
5. **Contact Determination**: If the batter swings, contact probability is calculated based on:
   - Pitcher quality vs. batter contact rating
   - Pitch location (center pitches have higher contact rates)
   - Random outcome
6. **At-Bat Resolution**: The sequence continues until:
   - 4 balls are thrown (walk)
   - 3 strikes are thrown (strikeout)
   - The batter makes contact (ball in play)

### Strike Zone Mechanics

The strike zone is defined by:
- **Width**: -0.85 to 0.85 (horizontal)
- **Height**: -2.0 to 1.5 (vertical)

Pitches are plotted on a 2D graph showing their location relative to this zone.

### Rating System

- **Pitcher Rating** (1-99): Affects pitch quality and batter contact probability
  - Higher ratings produce better pitches that are harder to hit
- **Batter Contact Rating** (1-99): Affects ability to make contact with pitches
  - Higher ratings increase contact probability against quality pitches

## Classes

### Player
Base class for all players. Stores basic player information.

**Attributes:**
- `name`: Player's full name
- `throwingHand`: 'Left' or 'Right'
- `battingHand`: 'Left', 'Right', or 'Switch'

### Pitcher (extends Player)
Represents a pitcher with specific pitching abilities.

**Attributes:**
- `pitchDict`: Dictionary of available pitches and their characteristics
- `energy`: Current energy level (0-100)
- `rating`: Pitcher skill rating (1-99)

**Methods:**
- `getRating()`: Returns pitcher's skill rating

### Batter (extends Player)
Represents a batter with contact and hitting abilities.

**Attributes:**
- `contact`: Contact rating (1-99)

**Methods:**
- `getRating()`: Returns batter's contact rating

### Pitch
Represents a single pitch thrown by the pitcher.

**Attributes:**
- `pitcher`: Reference to the Pitcher object
- `location`: Tuple (x, y) representing pitch location
- `pitch`: Type of pitch thrown
- `pitchQuality`: Quality rating of the pitch (90-100)

**Methods:**
- `getPitch()`: Returns pitch type
- `getLocation()`: Returns pitch location coordinates
- `getPitchQuality()`: Returns pitch quality rating
- `isStrike()`: Returns True if pitch is within strike zone

### Swing
Handles batter's swing decision and contact outcome.

**Attributes:**
- `currentPitch`: The Pitch object being evaluated
- `batter`: Reference to the Batter object
- `pitcher`: Reference to the Pitcher object
- `pitchQuality`: Quality of the current pitch

**Methods:**
- `swingOrTake(balls, strikes)`: Determines if batter swings based on count
- `swingContact()`: Determines if batter makes contact when swinging

## Example

```python
from atbat import Pitcher, Batter, atBat

# Create players
ace_pitcher = Pitcher('Clayton', 'Kershaw', 25, 'Left', 'Right', 95)
star_batter = Batter('Mike', 'Trout', 23, 'Right', 'Right', 92)

# Run the at-bat
atBat(ace_pitcher, star_batter)

# The simulator will:
# 1. Display each pitch and count
# 2. Show swing/take decisions
# 3. Display contact results
# 4. Plot all pitches on a graph with the strike zone
```

## Future Improvements

- **Fix Deprecated Print Statements**: Update Python 2 `print` statements to Python 3 compatible `print()` functions
- **Add More Pitch Types**: Implement curveballs, sliders, sinkers, and other pitch variations
- **Implement Base Running**: Add logic for runners on base and base running decisions
- **Batting Average Tracking**: Track statistics across multiple at-bats
- **Pitcher Fatigue**: Implement energy depletion affecting pitch quality over time
- **Handedness Advantage**: Add pitcher-batter handedness matchup effects
- **Improved Visualization**: Enhanced graphics with better strike zone representation
- **Game Simulation**: Extend to full game simulation with multiple at-bats and innings
- **Configuration File**: Allow customizable strike zone and pitch parameters
- **Unit Tests**: Add comprehensive test coverage for all classes and methods

## License

This project is open source and available for educational purposes.
