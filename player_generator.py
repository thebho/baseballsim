"""
player_generator.py - Generate random baseball players
"""

import random
from atbat import Pitcher, Batter
from players_data import TEAMS, BATTER_POSITIONS

# First names pool (50+)
FIRST_NAMES = [
    "James", "Robert", "Michael", "William", "David",
    "Richard", "Joseph", "Thomas", "Charles", "Christopher",
    "Daniel", "Matthew", "Anthony", "Mark", "Donald",
    "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
    "Kevin", "Brian", "George", "Edward", "Ronald",
    "Timothy", "Jason", "Jeffrey", "Ryan", "Jacob",
    "Gary", "Nicholas", "Eric", "Jonathan", "Stephen",
    "Larry", "Justin", "Scott", "Brandon", "Benjamin",
    "Samuel", "Frank", "Gregory", "Alexander", "Raymond",
    "Patrick", "Jack", "Dennis", "Jerry", "Tyler",
    "Aaron", "Jose", "Adam", "Henry", "Douglas"
]

# Last names pool (50+)
LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris",
    "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Peterson", "Phillips", "Campbell",
    "Parker", "Evans", "Edwards", "Collins", "Reeves",
    "Stewart", "Morris", "Morales", "Murphy", "Cook",
    "Rogers", "Gutierrez", "Ortiz", "Morgan", "Peterson"
]


class SessionPlayerTracker:
    """Tracks used jersey numbers for the current session"""
    
    def __init__(self):
        self.used_jerseys = set()
    
    def get_unique_jersey(self, low=1, high=99):
        """
        Get a unique jersey number in [low, high] not already used.
        Raises ValueError if all numbers in range are exhausted.
        """
        available = [n for n in range(low, high + 1) if n not in self.used_jerseys]
        if not available:
            raise ValueError(f"All jersey numbers in range [{low}, {high}] are exhausted")
        jersey = random.choice(available)
        self.used_jerseys.add(jersey)
        return jersey
    
    def reset(self):
        """Clear the set of used jersey numbers"""
        self.used_jerseys.clear()


def _generate_height():
    """Generate a random height in format X'Y\" between 5'8\" and 6'5\" inclusive"""
    # 5'8" = 68 inches, 6'5" = 77 inches
    total_inches = random.randint(68, 77)
    feet = total_inches // 12
    inches = total_inches % 12
    return f"{feet}'{inches}\""


def generate_random_pitcher(tracker=None):
    """
    Generate a random Pitcher instance.
    
    Args:
        tracker: Optional SessionPlayerTracker for unique jersey numbers
    
    Returns:
        A Pitcher instance with random attributes
    """
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    age = random.randint(18, 40)
    height = _generate_height()
    weight = random.randint(150, 260)
    throwing_hand = random.choice(["Left", "Right"])
    batting_hand = random.choice(["Left", "Right"])
    position = random.choice(["SP", "RP"])
    team = random.choice(TEAMS)
    jersey_number = tracker.get_unique_jersey() if tracker else random.randint(1, 99)
    experience = random.randint(0, 20)
    stamina = random.randint(30, 99)
    accuracy = random.randint(30, 99)
    velocity = random.randint(30, 99)
    pitch_variety = random.randint(30, 99)
    wins = random.randint(0, 300)
    losses = random.randint(0, 200)
    era = round(random.uniform(1.00, 6.00), 2)
    
    return Pitcher(
        firstName=first_name,
        lastName=last_name,
        throwingHand=throwing_hand,
        battingHand=batting_hand,
        age=age,
        height=height,
        weight=weight,
        position=position,
        team=team,
        jersey_number=jersey_number,
        experience_years=experience,
        stamina=stamina,
        accuracy=accuracy,
        velocity=velocity,
        pitch_variety=pitch_variety,
        wins=wins,
        losses=losses,
        era=era
    )


def generate_random_batter(tracker=None):
    """
    Generate a random Batter instance.
    
    Args:
        tracker: Optional SessionPlayerTracker for unique jersey numbers
    
    Returns:
        A Batter instance with random attributes
    """
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    age = random.randint(18, 40)
    height = _generate_height()
    weight = random.randint(150, 260)
    throwing_hand = random.choice(["Left", "Right"])
    batting_hand = random.choice(["Left", "Right"])
    position = random.choice(BATTER_POSITIONS)
    team = random.choice(TEAMS)
    jersey_number = tracker.get_unique_jersey() if tracker else random.randint(1, 99)
    experience = random.randint(0, 20)
    power = random.randint(30, 99)
    speed = random.randint(30, 99)
    plate_discipline = random.randint(30, 99)
    home_runs = random.randint(0, 500)
    hits = random.randint(0, 3000)
    strikeouts = random.randint(0, 2000)
    batting_average = round(random.uniform(0.150, 0.400), 3)
    
    return Batter(
        firstName=first_name,
        lastName=last_name,
        throwingHand=throwing_hand,
        battingHand=batting_hand,
        age=age,
        height=height,
        weight=weight,
        position=position,
        team=team,
        jersey_number=jersey_number,
        experience_years=experience,
        power=power,
        speed=speed,
        plate_discipline=plate_discipline,
        home_runs=home_runs,
        hits=hits,
        strikeouts=strikeouts,
        batting_average=batting_average
    )


def generate_random_player(player_type=None, tracker=None):
    """
    Generate a random player (pitcher or batter).
    
    Args:
        player_type: "pitcher", "batter", or None (random choice)
        tracker: Optional SessionPlayerTracker for unique jersey numbers
    
    Returns:
        A Pitcher or Batter instance
    """
    if player_type is None:
        player_type = random.choice(["pitcher", "batter"])
    
    if player_type == "pitcher":
        return generate_random_pitcher(tracker)
    elif player_type == "batter":
        return generate_random_batter(tracker)
    else:
        raise ValueError(f"Invalid player_type: {player_type}")


if __name__ == "__main__":
    tracker = SessionPlayerTracker()
    
    print("=" * 50)
    print("RANDOM PITCHER")
    print("=" * 50)
    pitcher = generate_random_pitcher(tracker)
    print(pitcher.get_info())
    print(pitcher.get_stats())
    
    print("\n" + "=" * 50)
    print("RANDOM BATTER")
    print("=" * 50)
    batter = generate_random_batter(tracker)
    print(batter.get_info())
    print(batter.get_stats())
