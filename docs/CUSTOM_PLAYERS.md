# Custom Players Guide

This guide explains how to create and use custom players in the Baseball Simulator.

## Overview

The Baseball Simulator supports two types of players:
- **Pitcher**: A player who throws pitches
- **Batter**: A player who hits pitches

Both inherit from the base `Player` class and can be customized with various attributes.

## Creating a Pitcher

### Syntax

```python
pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating)
```

### Parameters

| Parameter | Type | Description | Valid Values |
|-----------|------|-------------|--------------|
| `firstName` | string | Player's first name | Any string |
| `lastName` | string | Player's last name | Any string |
| `age` | integer | Player's age | Any positive integer |
| `throwingHand` | string | Hand used for throwing | `'Left'` or `'Right'` |
| `battingHand` | string | Hand used for batting | `'Left'`, `'Right'`, or `'Switch'` |
| `pitcherRating` | integer | Pitcher's skill rating | 1-99 (higher is better) |

### Example

```python
# Create a dominant pitcher
ace_pitcher = Pitcher('Clayton', 'Kershaw', 35, 'Left', 'Right', 95)

# Create a relief pitcher
relief_pitcher = Pitcher('Mariano', 'Rivera', 48, 'Right', 'Right', 92)

# Create a weaker pitcher
rookie_pitcher = Pitcher('John', 'Doe', 22, 'Right', 'Right', 45)
```

### Pitcher Attributes

After creation, a Pitcher object has the following attributes:

- `name`: Full name (firstName + lastName)
- `throwingHand`: Hand used for throwing
- `battingHand`: Hand used for batting
- `rating`: Pitcher's skill rating (1-99)
- `energy`: Current energy level (starts at 100)
- `pitchDict`: Dictionary of available pitches

### Pitcher Methods

- `getRating()`: Returns the pitcher's rating

## Creating a Batter

### Syntax

```python
batter = Batter(firstName, lastName, age, throwingHand, battingHand, contact)
```

### Parameters

| Parameter | Type | Description | Valid Values |
|-----------|------|-------------|--------------|
| `firstName` | string | Player's first name | Any string |
| `lastName` | string | Player's last name | Any string |
| `age` | integer | Player's age | Any positive integer |
| `throwingHand` | string | Hand used for throwing | `'Left'` or `'Right'` |
| `battingHand` | string | Hand used for batting | `'Left'`, `'Right'`, or `'Switch'` |
| `contact` | integer | Batter's contact rating | 1-99 (higher is better) |

### Example

```python
# Create an elite contact hitter
elite_batter = Batter('Stan', 'Musial', 38, 'Right', 'Right', 94)

# Create a power hitter
power_hitter = Batter('Babe', 'Ruth', 40, 'Left', 'Right', 88)

# Create a weak batter
weak_batter = Batter('Bad', 'Batter', 40, 'Left', 'Left', 40)
```

### Batter Attributes

After creation, a Batter object has the following attributes:

- `name`: Full name (firstName + lastName)
- `throwingHand`: Hand used for throwing
- `battingHand`: Hand used for batting
- `contact`: Batter's contact rating (1-99)

### Batter Methods

- `getRating()`: Returns the batter's contact rating

## Using Custom Players in At-Bats

Once you've created your custom players, you can simulate an at-bat between them:

```python
# Create custom players
my_pitcher = Pitcher('Max', 'Scherzer', 37, 'Right', 'Right', 96)
my_batter = Batter('Mike', 'Trout', 30, 'Right', 'Right', 92)

# Simulate an at-bat
atBat(my_pitcher, my_batter)
```

The `atBat()` function will:
1. Simulate pitches thrown by the pitcher
2. Determine if the batter swings or takes each pitch
3. Calculate contact if the batter swings
4. Continue until the batter gets a hit, walks, or strikes out
5. Display a visualization of all pitches thrown

## Rating Guidelines

### Pitcher Ratings (1-99)

- **90-99**: Elite pitchers (Hall of Famers, Cy Young winners)
- **80-89**: All-Star caliber pitchers
- **70-79**: Above average starting pitchers
- **60-69**: Average MLB pitchers
- **50-59**: Below average pitchers
- **40-49**: Weak pitchers
- **1-39**: Very poor pitchers

### Batter Contact Ratings (1-99)

- **90-99**: Elite contact hitters (Hall of Famers)
- **80-89**: All-Star caliber hitters
- **70-79**: Above average hitters
- **60-69**: Average MLB hitters
- **50-59**: Below average hitters
- **40-49**: Weak hitters
- **1-39**: Very poor hitters

## Tips for Creating Realistic Players

1. **Research real players**: Use actual MLB statistics as a reference for ratings
2. **Consider handedness**: Most players bat and throw with the same hand
3. **Use switch hitters**: Set `battingHand='Switch'` for versatile players
4. **Balance ratings**: Create a mix of strong and weak players for interesting simulations
5. **Age matters**: While not directly used in calculations, age can help track player progression

## Advanced: Modifying Player Attributes

You can modify player attributes after creation:

```python
pitcher = Pitcher('John', 'Doe', 25, 'Right', 'Right', 75)

# Modify the pitcher's energy (simulating fatigue)
pitcher.energy = 50

# Modify the pitcher's rating (simulating improvement)
pitcher.rating = 85
```

## Example: Creating a Full Roster

```python
# Create a pitching staff
starting_pitchers = [
    Pitcher('Ace', 'One', 30, 'Right', 'Right', 95),
    Pitcher('Ace', 'Two', 28, 'Right', 'Right', 92),
    Pitcher('Ace', 'Three', 26, 'Right', 'Right', 88),
]

# Create a batting lineup
batters = [
    Batter('Star', 'Player', 32, 'Right', 'Right', 94),
    Batter('Good', 'Hitter', 28, 'Left', 'Left', 85),
    Batter('Average', 'Player', 25, 'Right', 'Right', 70),
    Batter('Weak', 'Hitter', 35, 'Right', 'Right', 45),
]

# Simulate multiple at-bats
for pitcher in starting_pitchers:
    for batter in batters:
        print(f"\n{pitcher.name} vs {batter.name}")
        atBat(pitcher, batter)
```

## Troubleshooting

### Issue: Player name appears concatenated
**Solution**: The `name` attribute concatenates firstName and lastName without a space. This is expected behavior.

### Issue: Pitcher or Batter not responding as expected
**Solution**: Verify that ratings are between 1-99. Ratings outside this range may produce unexpected behavior.

### Issue: At-bat simulation not running
**Solution**: Ensure both pitcher and batter objects are properly instantiated before calling `atBat()`.

## See Also

- [README.md](../README.md) - Main project documentation
- [atbat.py](../atbat.py) - Source code for the simulator
