# Baseball Simulator

## Project Description

Baseball Simulator is a Python-based simulation of MLB at-bats with realistic pitch mechanics and batter decision-making. This project models the complex interactions between pitchers and batters, including pitch selection, location, quality, and batter responses based on game count situations.

## Features

- **Player/Pitcher/Batter Classes** – Object-oriented design with a base Player class and specialized Pitcher and Batter subclasses
- **Pitch Mechanics** – Realistic pitch generation with location (x, y coordinates) and quality ratings
- **Swing Logic** – Intelligent batter decision-making based on count (balls/strikes), pitch location, and pitch quality
- **Strike Zone Visualization** – Visual representation of the strike zone and all pitches thrown during an at-bat
- **At-Bat Simulation** – Complete at-bat sequences with realistic outcomes including walks, strikeouts, and balls in play
- **Pitch Quality Modeling** – Pitcher skill and energy affect pitch quality, which influences batter contact probability

## Requirements

- **Python 2.7+** (Note: The current code uses Python 2 print statements)
- **matplotlib/pylab** – For strike zone visualization and pitch plotting

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thebho/baseballsim.git
   cd baseballsim
   ```

2. Ensure matplotlib is installed:
   ```bash
   pip install matplotlib
   ```

## Usage

### Basic Example

Create a Pitcher and Batter object, then simulate an at-bat:

```python
# Create a pitcher: Bob Gibson, age 20, right-handed, pitcher rating 98
BobGibson = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)

# Create a batter: Stan Musial, age 20, right-handed, contact rating 94
StanMusial = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Run the at-bat simulation
atBat(BobGibson, StanMusial)
```

The simulation will:
1. Pitch until the batter reaches 4 balls (walk), 3 strikes (strikeout), or puts the ball in play
2. Display the count after each pitch
3. Show swing/take decisions and contact results
4. Display a visualization of all pitches thrown with the strike zone overlay

## Code Structure

### Player (Base Class)
The foundation class for all players. Stores basic player information including name, throwing hand, and batting hand.

### Pitcher (Extends Player)
Represents a MLB pitcher with:
- `pitchDict` – Dictionary of available pitches and their characteristics
- `energy` – Current energy level (affects pitch quality)
- `rating` – Pitcher skill rating (1-99)
- `getRating()` – Returns the pitcher's rating

### Batter (Extends Player)
Represents a MLB batter with:
- `contact` – Contact rating (1-99), affects ability to make contact on pitches
- `getRating()` – Returns the batter's contact rating

### Pitch
Generates and manages individual pitches:
- Randomly selects pitch type from pitcher's pitch dictionary
- Generates random location within the strike zone area
- Calculates pitch quality (0-100) based on pitcher skill
- `isStrike()` – Determines if a taken pitch is within the strike zone

### Swing
Handles batter decisions and contact:
- `swingOrTake(balls, strikes)` – Decides whether to swing based on count and pitch location
  - More aggressive (higher swing rate) with 0-0 count
  - More conservative (lower swing rate) with 3-0 count
  - Very aggressive with 2 strikes
- `swingContact()` – Determines if a swing results in contact
  - Pitcher advantage (quality - contact rating) affects contact probability
  - Better contact on pitches down the middle

### atBat(pitcher, batter)
Orchestrates a complete at-bat sequence:
1. Initializes balls, strikes, and pitch count
2. Loops until walk (4 balls), strikeout (3 strikes), or ball in play
3. For each pitch:
   - Creates a Pitch object
   - Creates a Swing object
   - Determines swing/take decision
   - If swing, determines contact
   - Updates count accordingly
4. Displays final result (walk, strikeout, or ball in play)
5. Visualizes all pitches with strike zone overlay

## Known Issues

1. **Incomplete Code at Bottom** – Lines 155-165 contain incomplete code with a `while Result==False:` loop that:
   - References undefined variable `PitchCount` (should be initialized)
   - Calls `S.swingOrTake()` without required `balls` and `strikes` parameters
   - This code appears to be leftover from development and should be removed or completed

2. **Python 2 Syntax** – The code uses Python 2 print statements (e.g., `print x, y` instead of `print(x, y)`)
   - Will not run on Python 3 without modification

3. **Minor Typo** – Example at line 152 creates a batter named 'Musical' instead of 'Musial'

## Future Improvements

- **Fix Incomplete Code** – Complete or remove the unfinished at-bat loop at the bottom of the file
- **Python 3 Migration** – Update all print statements to Python 3 syntax for broader compatibility
- **Unit Tests** – Add comprehensive test suite for Player, Pitcher, Batter, Pitch, and Swing classes
- **Expand Pitch Types** – Add more pitch types (curveball, slider, sinker, etc.) with different characteristics
- **Advanced Batter Logic** – Implement batter tendencies (aggressive vs. patient hitters, handedness matchups)
- **Game Statistics** – Track and display statistics across multiple at-bats (batting average, strikeout rate, etc.)
- **Pitcher Fatigue** – Implement energy depletion affecting pitch quality over time
- **Improved Visualization** – Add color coding for pitch types and swing results
