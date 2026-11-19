# Baseball At-Bat Simulator

## Project Description

BaseballSim is a baseball at-bat simulator that models realistic pitcher-batter interactions. The simulator generates pitches with varying types and locations, evaluates strike zone placement, and determines batter swing decisions and contact outcomes based on player ratings and game count situations.

## Features

- **Pitcher and Batter Classes**: Customizable player objects with individual ratings that affect gameplay
- **Pitch Selection and Location Simulation**: Randomly selects pitch types (Fastball, ChangeUp) and generates realistic pitch locations
- **Strike Zone Detection**: Accurately determines whether pitches fall within the official strike zone
- **Swing Decision Logic**: Batter swing/take decisions vary based on the ball-strike count
- **Contact Probability**: Contact outcomes calculated based on pitcher skill, batter contact rating, and pitch quality
- **Pitch Visualization**: Generates scatter plots showing all pitch locations during an at-bat with strike zone overlay
- **At-Bat Outcomes**: Simulates complete at-bats resulting in walks, strikeouts, or balls in play

## Requirements

- Python 2.7+
- `matplotlib` (pylab) - for pitch visualization
- `random` - for stochastic pitch and swing simulation
- `math` - for mathematical calculations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thebho/baseballsim.git
   cd baseballsim
   ```

2. Ensure you have matplotlib installed:
   ```bash
   pip install matplotlib
   ```

3. Run the simulator:
   ```bash
   python atbat.py
   ```

## Usage

### Basic Example

```python
from atbat import Pitcher, Batter, atBat

# Create a pitcher with high skill rating (1-99)
pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)

# Create a batter with high contact rating (1-99)
batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Run an at-bat simulation
atBat(pitcher, batter)
```

### Creating Players

**Pitcher:**
```python
pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating)
# pitcherRating: Integer 1-99 (higher = better pitcher)
# throwingHand: 'Left' or 'Right'
# battingHand: 'Left' or 'Right'
```

**Batter:**
```python
batter = Batter(firstName, lastName, age, throwingHand, battingHand, contactRating)
# contactRating: Integer 1-99 (higher = better contact hitter)
# throwingHand: 'Left' or 'Right'
# battingHand: 'Left', 'Right', or 'Switch'
```

### Running an At-Bat

```python
atBat(pitcher, batter)
```

This function simulates a complete at-bat and displays:
- Console output showing each pitch count, swing decisions, and at-bat result
- A visualization plot showing all pitch locations with the strike zone outlined

## How It Works

### Pitch Generation

Each pitch is generated with three components:

1. **Pitch Type**: Randomly selected from the pitcher's available pitches (Fastball, ChangeUp)
2. **Location**: Random coordinates within the strike zone area
3. **Quality**: A value between 90-100 representing pitch execution quality

### Strike Zone Rules

The strike zone is defined by boundaries:
- **Horizontal**: -0.85 to 0.85 (relative to center)
- **Vertical**: -2.0 to 1.5 (relative to center)

Pitches outside these boundaries are called balls; pitches inside are strikes if not swung at.

### Swing/Take Decision Logic

The batter's decision to swing or take a pitch depends on the count:

- **0-0 Count**: 80% take rate (patient approach)
- **3-0 Count**: 90% take rate (very selective)
- **0-2 Count**: 10% take rate (must protect)
- **Other Counts**: 50% take rate (neutral)

Additionally, batters are more likely to swing at pitches in the heart of the zone and less likely to swing at pitches on the edges.

### Contact Probability

When a batter swings, contact is determined by:

1. **Pitch Location**: Pitches down the middle (-0.6 to 0.6 horizontally, -2.0 to 1.5 vertically) result in automatic contact
2. **Pitcher Advantage**: Calculated as `pitchQuality - batterContactRating`
   - Advantage > 10: 95% miss rate
   - Advantage 0-10: 50% miss rate
   - Advantage -10 to 0: 30% miss rate
   - Advantage < -10: Automatic contact

### At-Bat Outcomes

An at-bat ends when one of three conditions is met:

- **Walk (Base on Balls)**: 4 balls accumulated
- **Strikeout**: 3 strikes accumulated
- **Ball in Play**: Batter makes contact on a swing

## Project Status

⚠️ **Note**: The `Player`, `Pitcher`, and `Batter` classes are marked as temporary and may be refactored in future versions. The core simulation logic in the `Pitch`, `Swing`, and `atBat` functions is the primary focus of the project.

## Future Improvements

- **Hit Outcome Simulation**: Implement realistic hit outcomes (single, double, triple, home run) based on batter power and pitcher quality
- **Additional Pitch Types**: Expand beyond Fastball and ChangeUp to include Curveball, Slider, Sinker, etc.
- **Handedness Matchup Effects**: Adjust contact probability and swing rates based on pitcher-batter handedness matchups
- **Energy/Fatigue Effects**: Simulate pitcher fatigue affecting pitch quality and velocity over multiple at-bats
- **Statistical Tracking**: Accumulate season statistics for players across multiple at-bats
- **Advanced Visualization**: Enhanced graphics showing pitch movement, velocity, and spin rate
- **Machine Learning Integration**: Train models to predict optimal pitch selection and batter approach

## License

This project is open source and available under the MIT License.
