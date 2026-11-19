# AGENTS.md - Repository Interaction Guide

## Overview

This repository contains **baseballsim**, a Python-based baseball simulation engine. It models at-bat sequences between pitchers and batters, including pitch selection, location, swing decisions, and contact outcomes.

## Repository Structure

- **atbat.py** - Main simulation module containing:
  - `Player`, `Pitcher`, `Batter` classes for player representation
  - `Pitch` class for pitch mechanics and strike zone logic
  - `Swing` class for batter decision-making and contact
  - `atBat()` function to simulate a complete at-bat sequence

## How to Interact

### Running the Simulation

```bash
python atbat.py
```

This executes the default simulation with:
- **Pitcher**: Bob Gibson (rating 98)
- **Batter**: Stan Musial (rating 94)

The simulation outputs:
- Ball/strike count progression
- Pitch types and locations
- At-bat outcome (walk, strikeout, or ball in play)
- Visualization of pitch locations relative to the strike zone

### Creating Custom Simulations

Import and use the classes directly:

```python
from atbat import Pitcher, Batter, atBat

# Create players
pitcher = Pitcher('Name', 'Surname', age, 'Right'/'Left', 'Right'/'Left', rating)
batter = Batter('Name', 'Surname', age, 'Right'/'Left', 'Right'/'Left', contact_rating)

# Run simulation
atBat(pitcher, batter)
```

### Key Parameters

**Pitcher Rating**: 1-99 (affects pitch quality and strikeout likelihood)
**Batter Contact**: 1-99 (affects ability to make contact with pitches)
**Batting Hand**: 'Left', 'Right', or 'Switch'
**Throwing Hand**: 'Left' or 'Right'

## Simulation Logic

### Pitch Generation
- Randomly selects pitch type from pitcher's repertoire (Fastball, ChangeUp)
- Assigns random location within strike zone boundaries
- Calculates pitch quality (90-100 scale)

### Batter Decision
- Evaluates pitch location and count situation
- Decides to swing or take based on probability thresholds
- Adjusts strategy based on balls/strikes (e.g., more aggressive at 3-0)

### Contact Outcome
- Determines if swing results in contact
- Probability influenced by pitch quality vs. batter contact rating
- Pitcher advantage > 10: 95% strikeout rate
- Pitcher advantage < -10: 100% contact rate

### At-Bat Resolution
- Continues until walk (4 balls), strikeout (3 strikes), or ball in play
- Outputs pitch sequence visualization

## Development Notes

- **Dependencies**: `random`, `math`, `pylab` (matplotlib)
- **Python Version**: 2.x (uses `print` statements without parentheses)
- **Strike Zone**: Defined as (-0.85, 0.85, -2.0, 1.5) in normalized coordinates

## Contributing

When modifying this repository:
1. Maintain backward compatibility with existing `Player`, `Pitcher`, `Batter` classes
2. Update pitch mechanics in the `Pitch` class carefully (affects all simulations)
3. Test changes with the default `atBat(BobGibson, StanMusial)` call
4. Add new pitch types to `PITCH_DICT` with skill modifier and color for visualization
5. Document any changes to decision-making logic in `Swing` class

## Future Enhancements

Potential areas for expansion:
- Baserunning and game state simulation
- Multiple at-bats and full game simulation
- Player statistics tracking and persistence
- Advanced pitch movement and spin rates
- Batter-pitcher matchup history
- Improved visualization with matplotlib
