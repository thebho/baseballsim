"""
Baseball players database with 100 real MLB players from various teams.

Defines Player, Pitcher, and Batter classes compatible with atbat.py,
and provides a roster of 100 real MLB players (50 pitchers, 50 batters).
"""


class Player(object):
    """Creates a MLB player."""

    def __init__(self, firstName, lastName, throwingHand, battingHand):
        """
        battingHand='Left', 'Right', 'Switch'
        throwingHand='Left', 'Right'
        """
        self.name = str(firstName) + ' ' + str(lastName)
        self.throwingHand = throwingHand
        self.battingHand = battingHand


class Pitcher(Player):
    """A MLB pitcher. Subclass of Player."""

    PITCH_DICT = {'Fastball': [0.97, 'r'], 'ChangeUp': [0.95, 'b']}

    def __init__(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating):
        """
        Creates a Pitcher instance.
        pitcherRating = an integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand)
        self.pitchDict = self.PITCH_DICT.copy()
        self.age = age
        self.energy = 100
        self.rating = pitcherRating

    def getRating(self):
        return self.rating


class Batter(Player):
    """A MLB batter. Subclass of Player."""

    def __init__(self, firstName, lastName, age, throwingHand, battingHand, contact):
        """
        Creates a Batter instance.
        contact = an integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand)
        self.age = age
        self.contact = contact

    def getRating(self):
        """Returns a batter's contact rating."""
        return self.contact


# ---------------------------------------------------------------------------
# 50 real MLB pitchers
# (firstName, lastName, age, throwingHand, battingHand, rating)
# ---------------------------------------------------------------------------
pitchers = [
    # Los Angeles Dodgers
    Pitcher('Clayton', 'Kershaw',    35, 'Left',  'Right', 96),
    Pitcher('Walker',  'Buehler',    28, 'Right', 'Right', 90),
    Pitcher('Julio',   'Urias',      26, 'Left',  'Left',  88),
    Pitcher('Tony',    'Gonsolin',   29, 'Right', 'Right', 91),
    Pitcher('Evan',    'Phillips',   26, 'Right', 'Right', 89),
    # New York Yankees
    Pitcher('Gerrit',  'Cole',       32, 'Right', 'Right', 96),
    Pitcher('Nestor',  'Cortes',     28, 'Left',  'Left',  90),
    Pitcher('Carlos',  'Rodon',      30, 'Left',  'Left',  91),
    Pitcher('Luis',    'Severino',   29, 'Right', 'Right', 89),
    Pitcher('Garrett', 'Whitlock',   27, 'Right', 'Right', 86),
    # Houston Astros
    Pitcher('Framber', 'Valdez',     28, 'Left',  'Left',  91),
    Pitcher('Cristian','Javier',     27, 'Right', 'Right', 90),
    Pitcher('Hunter',  'Brown',      24, 'Right', 'Right', 86),
    Pitcher('Ronel',   'Blanco',     28, 'Right', 'Right', 87),
    Pitcher('Josh',    'Hader',      29, 'Left',  'Left',  93),
    # Atlanta Braves
    Pitcher('Spencer', 'Strider',    25, 'Right', 'Right', 93),
    Pitcher('Max',     'Fried',      30, 'Left',  'Left',  91),
    Pitcher('Kyle',    'Wright',     27, 'Right', 'Right', 88),
    Pitcher('Bryce',   'Elder',      24, 'Right', 'Right', 85),
    Pitcher('A.J.',    'Minter',     29, 'Left',  'Left',  87),
    # Milwaukee Brewers
    Pitcher('Corbin',  'Burnes',     28, 'Right', 'Right', 94),
    Pitcher('Brandon', 'Woodruff',   30, 'Right', 'Right', 92),
    Pitcher('Freddy',  'Peralta',    27, 'Right', 'Right', 89),
    Pitcher('Devin',   'Williams',   28, 'Right', 'Right', 88),
    Pitcher('Brent',   'Suter',      34, 'Left',  'Left',  87),
    # San Francisco Giants
    Pitcher('Logan',   'Webb',       27, 'Right', 'Right', 89),
    Pitcher('Kevin',   'Gausman',    32, 'Right', 'Right', 90),
    Pitcher('Blake',   'Snell',      31, 'Left',  'Left',  92),
    Pitcher('Alex',    'Cobb',       36, 'Right', 'Right', 84),
    Pitcher('Camilo',  'Doval',      25, 'Right', 'Right', 87),
    # Philadelphia Phillies
    Pitcher('Zack',    'Wheeler',    33, 'Right', 'Right', 91),
    Pitcher('Aaron',   'Nola',       30, 'Right', 'Right', 91),
    Pitcher('Ranger',  'Suarez',     27, 'Left',  'Left',  88),
    Pitcher('Taijuan', 'Walker',     31, 'Right', 'Right', 85),
    Pitcher('Craig',   'Kimbrel',    35, 'Right', 'Right', 86),
    # Cleveland Guardians
    Pitcher('Shane',   'Bieber',     28, 'Right', 'Right', 93),
    Pitcher('Triston', 'McKenzie',   26, 'Right', 'Right', 88),
    Pitcher('Cal',     'Quantrill',  28, 'Right', 'Right', 87),
    Pitcher('Tanner',  'Bibee',      24, 'Right', 'Right', 86),
    Pitcher('Emmanuel','Clase',      26, 'Right', 'Right', 91),
    # Arizona Diamondbacks
    Pitcher('Zac',     'Gallen',     28, 'Right', 'Right', 90),
    Pitcher('Merrill', 'Kelly',      35, 'Right', 'Right', 89),
    Pitcher('Brandon', 'Pfaadt',     24, 'Right', 'Right', 85),
    Pitcher('Paul',    'Sewald',     33, 'Right', 'Right', 87),
    Pitcher('Miguel',  'Castro',     28, 'Right', 'Right', 84),
    # Pittsburgh Pirates
    Pitcher('Paul',    'Skenes',     22, 'Right', 'Right', 89),
    Pitcher('Jared',   'Jones',      23, 'Right', 'Right', 87),
    Pitcher('Mitch',   'Keller',     27, 'Right', 'Right', 88),
    Pitcher('Martin',  'Perez',      32, 'Left',  'Left',  85),
    Pitcher('David',   'Bednar',     28, 'Right', 'Right', 88),
]

# ---------------------------------------------------------------------------
# 50 real MLB batters
# (firstName, lastName, age, throwingHand, battingHand, contact)
# ---------------------------------------------------------------------------
batters = [
    # Los Angeles Angels / Dodgers
    Batter('Mike',       'Trout',       32, 'Right', 'Right',  98),
    Batter('Mookie',     'Betts',       31, 'Right', 'Right',  96),
    Batter('Freddie',    'Freeman',     34, 'Left',  'Right',  93),
    Batter('Will',       'Smith',       28, 'Right', 'Right',  88),
    Batter('Max',        'Muncy',       33, 'Right', 'Left',   85),
    # New York Yankees
    Batter('Aaron',      'Judge',       32, 'Right', 'Right',  95),
    Batter('Giancarlo',  'Stanton',     34, 'Right', 'Right',  88),
    Batter('Anthony',    'Volpe',       23, 'Right', 'Right',  81),
    Batter('Gleyber',    'Torres',      27, 'Right', 'Right',  84),
    Batter('Harrison',   'Bader',       29, 'Right', 'Right',  83),
    # Houston Astros
    Batter('Jose',       'Altuve',      34, 'Right', 'Right',  91),
    Batter('Kyle',       'Tucker',      27, 'Right', 'Right',  90),
    Batter('Yordan',     'Alvarez',     26, 'Right', 'Left',   94),
    Batter('Alex',       'Bregman',     30, 'Right', 'Right',  89),
    Batter('Chas',       'McCormick',   28, 'Right', 'Right',  84),
    # Atlanta Braves
    Batter('Ronald',     'Acuna Jr.',   26, 'Right', 'Right',  95),
    Batter('Ozzie',      'Albies',      27, 'Right', 'Switch', 88),
    Batter('Austin',     'Riley',       26, 'Right', 'Right',  90),
    Batter('Matt',       'Olson',       30, 'Left',  'Left',   89),
    Batter('Michael',    'Harris II',   23, 'Right', 'Left',   85),
    # Philadelphia Phillies
    Batter('Bryce',      'Harper',      31, 'Left',  'Right',  94),
    Batter('Trea',       'Turner',      31, 'Right', 'Right',  88),
    Batter('Kyle',       'Schwarber',   31, 'Left',  'Right',  89),
    Batter('Nick',       'Castellanos', 32, 'Right', 'Right',  86),
    Batter('J.T.',       'Realmuto',    33, 'Right', 'Right',  91),
    # San Diego Padres
    Batter('Juan',       'Soto',        25, 'Right', 'Left',   97),
    Batter('Manny',      'Machado',     31, 'Right', 'Right',  91),
    Batter('Xander',     'Bogaerts',    31, 'Right', 'Right',  89),
    Batter('Fernando',   'Tatis Jr.',   25, 'Right', 'Right',  90),
    Batter('Jake',       'Cronenworth', 30, 'Right', 'Left',   84),
    # St. Louis Cardinals
    Batter('Paul',       'Goldschmidt', 36, 'Right', 'Right',  92),
    Batter('Nolan',      'Arenado',     33, 'Right', 'Right',  90),
    Batter('Willson',    'Contreras',   31, 'Right', 'Right',  85),
    Batter('Lars',       'Nootbaar',    26, 'Right', 'Right',  83),
    Batter('Tommy',      'Edman',       28, 'Right', 'Switch', 86),
    # Cleveland Guardians
    Batter('Jose',       'Ramirez',     31, 'Right', 'Switch', 93),
    Batter('Josh',       'Naylor',      26, 'Left',  'Left',   85),
    Batter('Steven',     'Kwan',        26, 'Right', 'Left',   87),
    Batter('Andres',     'Gimenez',     25, 'Right', 'Left',   84),
    Batter('David',      'Fry',         27, 'Right', 'Right',  80),
    # Tampa Bay Rays
    Batter('Randy',      'Arozarena',   28, 'Right', 'Right',  89),
    Batter('Yandy',      'Diaz',        32, 'Right', 'Right',  87),
    Batter('Isaac',      'Paredes',     25, 'Right', 'Right',  83),
    Batter('Brandon',    'Lowe',        29, 'Right', 'Left',   85),
    Batter('Jose',       'Siri',        28, 'Right', 'Right',  80),
    # Minnesota Twins
    Batter('Byron',      'Buxton',      30, 'Right', 'Right',  87),
    Batter('Luis',       'Arraez',      26, 'Right', 'Left',   89),
    Batter('Carlos',     'Correa',      29, 'Right', 'Right',  88),
    Batter('Jose',       'Miranda',     26, 'Right', 'Right',  84),
    Batter('Royce',      'Lewis',       24, 'Right', 'Right',  85),
]

# ---------------------------------------------------------------------------
# Combined roster
# ---------------------------------------------------------------------------
all_players = pitchers + batters


def get_all_pitchers():
    """Returns the list of all Pitcher objects."""
    return pitchers


def get_all_batters():
    """Returns the list of all Batter objects."""
    return batters


def get_all_players():
    """Returns the combined list of all Player objects."""
    return all_players


def get_player_count():
    """Returns the total number of players."""
    return len(all_players)


def get_pitcher_count():
    """Returns the total number of pitchers."""
    return len(pitchers)


def get_batter_count():
    """Returns the total number of batters."""
    return len(batters)
