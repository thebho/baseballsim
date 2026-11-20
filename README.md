# Baseball Sim

A baseball simulation project with player generation and management tools.

## Features

### Player Generator (`player_generator.py`)

A Python module for generating random baseball players with realistic attributes.

#### Components

- **`SessionPlayerTracker`**: Manages unique jersey numbers for a session
  - `get_unique_jersey(low=1, high=99)`: Returns a unique jersey number in the specified range
  - `reset()`: Clears all tracked jersey numbers

- **`generate_random_pitcher(tracker=None)`**: Generates a random pitcher with:
  - Basic info: name, age, height, weight, hands
  - Position: SP (Starting Pitcher) or RP (Relief Pitcher)
  - Team assignment
  - Attributes: stamina, accuracy, velocity, pitch variety (30–99 each)
  - Career stats: wins, losses, ERA

- **`generate_random_batter(tracker=None)`**: Generates a random batter with:
  - Basic info: name, age, height, weight, hands
  - Position: C, 1B, 2B, 3B, SS, LF, CF, RF, or DH
  - Team assignment
  - Attributes: power, speed, plate discipline (30–99 each)
  - Career stats: home runs, hits, strikeouts, batting average

- **`generate_random_player(player_type=None, tracker=None)`**: Generates either a pitcher or batter
  - If `player_type` is `None`, randomly chooses between pitcher and batter

#### Usage

```python
from player_generator import generate_random_pitcher, generate_random_batter, SessionPlayerTracker

# Generate players without jersey deduplication
pitcher = generate_random_pitcher()
batter = generate_random_batter()

# Generate players with unique jersey numbers
tracker = SessionPlayerTracker()
pitcher = generate_random_pitcher(tracker)
batter = generate_random_batter(tracker)

# Generate a random player type
player = generate_random_player(tracker=tracker)
```

Run the module directly to generate and display one random pitcher and one random batter:

```bash
python player_generator.py
```

### Web UI (`ui/`)

A simple, browser-based interface for viewing and generating players.

#### Files

- **`index.html`**: Main page structure
- **`app.js`**: Player management and generation logic
- **`style.css`**: Responsive styling with gradient theme

#### Features

- **Add Random Player**: Generate a new pitcher or batter with a single click
- **Player Cards**: Display each player's info and stats in an organized card layout
- **Statistics Dashboard**: Shows total players, pitcher count, and batter count
- **Persistent Storage**: Players are saved to browser localStorage
- **Remove Players**: Delete individual players or clear all at once
- **Responsive Design**: Works on desktop and mobile devices

#### Usage

Open `ui/index.html` in any web browser. No server or build process required.

The UI generates players independently using embedded JavaScript logic (not connected to the Python module).

---

## Project Structure

```
.
├── player_generator.py      # Python player generation module
├── ui/
│   ├── index.html          # Web UI main page
│   ├── app.js              # Player manager and generation logic
│   └── style.css           # Styling
└── README.md               # This file
```

## Requirements

- Python 3.6+ (for `player_generator.py`)
- Modern web browser (for `ui/`)

## License

See LICENSE file for details.
