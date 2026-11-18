# Baseball Simulator

A Python-based baseball at-bat simulator that models the interaction between a pitcher and batter, including pitch selection, location, swing decisions, and contact outcomes.

## Overview

This project simulates realistic baseball at-bats by:
- **Pitcher mechanics**: Selecting pitch types (Fastball, ChangeUp) with varying quality based on pitcher skill and energy
- **Pitch location**: Randomly placing pitches within and around the strike zone
- **Batter decisions**: Determining whether to swing or take based on count, pitch location, and batter skill
- **Contact outcomes**: Calculating swing-and-miss vs. contact based on pitcher advantage and batter contact rating
- **Visualization**: Plotting all pitches thrown during an at-bat with the strike zone overlay

## Features

- **Player Classes**: `Player`, `Pitcher`, and `Batter` objects with customizable attributes
- **Pitch Simulation**: Realistic pitch types with quality variance
- **Strike Zone Logic**: Accurate strike zone boundaries and pitch evaluation
- **Swing Logic**: Context-aware swing decisions based on ball/strike count
- **Contact Mechanics**: Pitcher vs. batter skill matchup determines contact probability
- **Visual Output**: Matplotlib visualization of pitch locations during an at-bat

## Requirements

- Python 2.7+ (note: code uses Python 2 syntax)
- `matplotlib` (for visualization)

## Installation

```bash
pip install matplotlib
```

## Usage

Run the simulator:

```bash
python atbat.py
```

### Creating Players

```python
# Create a pitcher (name, age, throwing hand, batting hand, rating 1-99)
pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)

# Create a batter (name, age, throwing hand, batting hand, contact rating 1-99)
batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Simulate an at-bat
atBat(pitcher, batter)
```

### Output

The simulator will:
1. Print each pitch type and count progression (balls/strikes)
2. Display swing decisions and outcomes
3. Show final result (Base on Balls, Strike Out, or Ball in Play)
4. Display a scatter plot of all pitches with the strike zone boundary

## How It Works

### At-Bat Sequence

1. **Pitch Generation**: Pitcher throws a pitch with random type and location
2. **Swing Decision**: Batter decides to swing or take based on:
   - Current ball/strike count
   - Pitch location relative to strike zone
   - Random probability factor
3. **Contact Determination**: If swinging, batter attempts contact based on:
   - Pitch quality vs. batter contact rating
   - Pitch location (center pitches = automatic contact)
4. **Count Update**: 
   - If taken: strike if in zone, ball if outside
   - If swung and missed: strike
   - If contact made: ball in play (at-bat ends)
5. **At-Bat End**: Continues until 4 balls (walk), 3 strikes (strikeout), or ball in play

### Skill System

- **Pitcher Rating** (1-99): Affects pitch quality and pitcher advantage
- **Batter Contact** (1-99): Affects ability to make contact on pitches outside the zone
- **Pitch Quality**: Randomly generated (90-100 range) and compared to batter rating

## Example Players

The script includes example players:
- **Bob Gibson** (Pitcher): Rating 98 - Hall of Famer
- **Stan Musial** (Batter): Contact 94 - Hall of Famer
- **Bad Batter**: Contact 40 - Struggling player

## Notes

- This is a work-in-progress simulator with placeholder classes
- Pitch types are currently limited to Fastball and ChangeUp
- The visualization uses matplotlib's interactive display
- Code uses Python 2 syntax (consider updating to Python 3)

## Future Enhancements

- Additional pitch types (Curveball, Slider, etc.)
- Pitcher fatigue/energy system
- Batter handedness advantages
- Hit outcome simulation (single, double, home run, etc.)
- Pitcher-batter matchup history
- Statistical tracking across multiple at-bats
