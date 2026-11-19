"""
Baseball players module containing fictional MLB players for the baseball simulation.
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


# Player roster
PITCHERS = [
    ThunderStrike(),
    SilentAssassin(),
    IceBreaker(),
    VenomFang(),
    ShadowCaster(),
]

BATTERS = [
    IronHammer(),
    SwiftBlade(),
    PhantomStrike(),
    CrimsonRush(),
    GoldenEagle(),
]

ALL_PLAYERS = PITCHERS + BATTERS
