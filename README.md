# Baseball Simulator

A Python-based baseball simulation that models at-bat sequences, pitch mechanics, and batter-pitcher interactions.

## Overview

This project simulates realistic baseball at-bats by modeling:
- Pitcher mechanics and pitch selection
- Batter decision-making (swing vs. take)
- Contact probability based on pitcher skill and batter contact rating
- Strike zone visualization

## Features

- **Player Classes**: Support for Pitcher and Batter player types with customizable attributes
- **Pitch Simulation**: Realistic pitch generation with location and quality metrics
- **Swing Logic**: Intelligent batter decision-making based on count and pitch location
- **Visualization**: Matplotlib-based visualization of pitch locations and strike zone

## Getting Started

### Requirements

- Python 2.7+
- matplotlib (pylab)

### Usage

```python
from atbat import Pitcher, Batter, atBat

# Create players
pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)
batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)

# Simulate an at-bat
atBat(pitcher, batter)
```

## Project Structure

- `atbat.py` - Main simulation module containing all classes and logic

## Classes

### Player
Base class for all players with name, throwing hand, and batting hand attributes.

### Pitcher
Extends Player with:
- `pitchDict`: Available pitches
- `energy`: Current energy level (0-100)
- `rating`: Pitcher skill rating (1-99)

### Batter
Extends Player with:
- `contact`: Contact rating (1-99)

### Pitch
Represents a single pitch with:
- Location relative to strike zone
- Pitch type (Fastball, ChangeUp, etc.)
- Quality rating

### Swing
Handles batter decision-making:
- `swingOrTake()`: Determines if batter swings
- `swingContact()`: Determines if swing makes contact

## ADA Compliance

This project is committed to accessibility and compliance with the Americans with Disabilities Act (ADA). We strive to ensure that our software is usable by everyone, including individuals with disabilities.

### Accessibility Features

- **Code Documentation**: Comprehensive docstrings and comments throughout the codebase to aid understanding
- **Clear Variable Naming**: Descriptive variable and function names that are easy to understand
- **Modular Design**: Well-organized class structure that is easy to navigate and modify

### Accessibility Considerations

- **Command-Line Interface**: The current implementation is text-based, making it compatible with screen readers
- **Visualization Output**: Matplotlib visualizations are generated as standard image files that can be processed by accessibility tools
- **Data Output**: All simulation results are printed to console in text format for easy access

### Future Accessibility Improvements

We are committed to improving accessibility in future versions:
- Enhanced alt-text descriptions for visualizations
- Web-based interface with WCAG 2.1 AA compliance
- Audio output options for simulation results
- Keyboard-only navigation support
- High contrast display options

### Accessibility Standards

This project aims to comply with:
- **WCAG 2.1**: Web Content Accessibility Guidelines (for future web implementations)
- **Section 508**: U.S. Federal accessibility requirements
- **ADA Title III**: Americans with Disabilities Act requirements for digital accessibility

### Reporting Accessibility Issues

If you encounter any accessibility barriers or have suggestions for improvement, please open an issue on the project repository with the label "accessibility". We welcome feedback and are committed to making continuous improvements.

### Resources

- [ADA.gov](https://www.ada.gov/) - Official ADA information
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Web accessibility guidelines
- [WebAIM](https://webaim.org/) - Web accessibility resources

## License

[Add your license information here]

## Contributing

Contributions are welcome! Please ensure any new features maintain accessibility standards.
