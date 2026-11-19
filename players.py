"""
Baseball players module containing fictional MLB players and retired St. Louis Cardinals for the baseball simulation.
"""

from atbat import Pitcher, Batter


# Fictional Pitchers
class ThunderStrike(Pitcher):
    """Elite power pitcher with exceptional fastball"""
    def __init__(self):
        super(ThunderStrike, self).__init__('Thunder', 'Strike', 28, 'Right', 'Right', 96)


class SilentAssassin(Pitcher):
    """Crafty left-handed pitcher with excellent control"""
    def __init__(self):
        super(SilentAssassin, self).__init__('Silent', 'Assassin', 34, 'Left', 'Right', 92)


class IceBreaker(Pitcher):
    """Dominant pitcher known for breaking balls"""
    def __init__(self):
        super(IceBreaker, self).__init__('Ice', 'Breaker', 26, 'Right', 'Left', 94)


class VenomFang(Pitcher):
    """Aggressive young pitcher with high velocity"""
    def __init__(self):
        super(VenomFang, self).__init__('Venom', 'Fang', 23, 'Right', 'Right', 88)


class ShadowCaster(Pitcher):
    """Veteran pitcher with years of experience"""
    def __init__(self):
        super(ShadowCaster, self).__init__('Shadow', 'Caster', 38, 'Left', 'Left', 85)


# Fictional Batters
class IronHammer(Batter):
    """Powerful slugger with exceptional contact"""
    def __init__(self):
        super(IronHammer, self).__init__('Iron', 'Hammer', 31, 'Right', 'Right', 95)


class SwiftBlade(Batter):
    """Quick-handed batter with excellent bat control"""
    def __init__(self):
        super(SwiftBlade, self).__init__('Swift', 'Blade', 27, 'Left', 'Left', 91)


class PhantomStrike(Batter):
    """Elusive batter with high contact rate"""
    def __init__(self):
        super(PhantomStrike, self).__init__('Phantom', 'Strike', 29, 'Right', 'Left', 89)


class CrimsonRush(Batter):
    """Aggressive young batter with growing skills"""
    def __init__(self):
        super(CrimsonRush, self).__init__('Crimson', 'Rush', 24, 'Left', 'Right', 82)


class GoldenEagle(Batter):
    """Veteran batter with consistent performance"""
    def __init__(self):
        super(GoldenEagle, self).__init__('Golden', 'Eagle', 36, 'Right', 'Right', 87)


# Retired St. Louis Cardinals Pitchers
class BobGibson(Pitcher):
    """Hall of Famer, dominant Cardinals pitcher with fierce competitiveness"""
    def __init__(self):
        super(BobGibson, self).__init__('Bob', 'Gibson', 45, 'Right', 'Right', 98)


class StanMusial(Pitcher):
    """Legendary Cardinals player, exceptional all-around athlete"""
    def __init__(self):
        super(StanMusial, self).__init__('Stan', 'Musial', 42, 'Left', 'Left', 94)


class OzzieSmiths(Pitcher):
    """Wizard of Oz, Cardinals shortstop with incredible defensive skills"""
    def __init__(self):
        super(OzzieSmiths, self).__init__('Ozzie', 'Smith', 40, 'Right', 'Right', 88)


class LouBrock(Pitcher):
    """Speed demon and base-stealing legend of the Cardinals"""
    def __init__(self):
        super(LouBrock, self).__init__('Lou', 'Brock', 43, 'Left', 'Left', 91)


class RogersHornsby(Pitcher):
    """Rajah, one of the greatest hitters in Cardinals history"""
    def __init__(self):
        super(RogersHornsby, self).__init__('Rogers', 'Hornsby', 48, 'Right', 'Right', 96)


# Retired St. Louis Cardinals Batters
class YadiMolina(Batter):
    """Future Hall of Famer, Cardinals catcher and leader"""
    def __init__(self):
        super(YadiMolina, self).__init__('Yadier', 'Molina', 41, 'Right', 'Right', 93)


class AlbertPujols(Batter):
    """Machine, Cardinals legend with incredible consistency and power"""
    def __init__(self):
        super(AlbertPujols, self).__init__('Albert', 'Pujols', 43, 'Right', 'Right', 97)


class ScottRolen(Batter):
    """Uber, Cardinals third baseman with elite defense and power"""
    def __init__(self):
        super(ScottRolen, self).__init__('Scott', 'Rolen', 48, 'Right', 'Right', 92)


class JimEdmonds(Batter):
    """Steady Eddie, Cardinals center fielder with grace and power"""
    def __init__(self):
        super(JimEdmonds, self).__init__('Jim', 'Edmonds', 50, 'Left', 'Left', 90)


class MarcMcGwire(Batter):
    """Big Mac, Cardinals slugger who captivated the nation"""
    def __init__(self):
        super(MarcMcGwire, self).__init__('Marc', 'McGwire', 56, 'Right', 'Right', 99)


# Player roster
PITCHERS = [
    ThunderStrike(),
    SilentAssassin(),
    IceBreaker(),
    VenomFang(),
    ShadowCaster(),
    BobGibson(),
    StanMusial(),
    OzzieSmiths(),
    LouBrock(),
    RogersHornsby(),
]

BATTERS = [
    IronHammer(),
    SwiftBlade(),
    PhantomStrike(),
    CrimsonRush(),
    GoldenEagle(),
    YadiMolina(),
    AlbertPujols(),
    ScottRolen(),
    JimEdmonds(),
    MarcMcGwire(),
]

ALL_PLAYERS = PITCHERS + BATTERS
