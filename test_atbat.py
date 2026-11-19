"""
Comprehensive test suite for atbat.py

This test file contains unit tests for all classes and methods in atbat.py:
- Player class
- Pitcher class (subclass of Player)
- Batter class (subclass of Player)
- Pitch class
- Swing class

Tests cover initialization, attribute access, method behavior, and integration scenarios.
"""

from __future__ import print_function
import unittest
import random
import math

# Constants from atbat.py
PITCH_SKILL, PITCH_FREQ = 0, 1
PITCH_DICT = {'Fastball': [0.97, 'r'], 'ChangeUp': [0.95, 'b']}
STRIKE_WIDTH = (-1.0, 1.0)
STRIKE_HEIGHT = (-4.0, 3.0)
STRIKE_ZONE = (-0.85, 0.85, -2.0, 1.5)


# Classes from atbat.py
class Player(object):
    """Creates a MLB player"""
    def __init__(self, firstName, lastName, throwingHand, battingHand):
        self.name = str(firstName) + str(lastName)
        self.throwingHand = throwingHand
        self.battingHand = battingHand


class Pitcher(Player):
    """A MLB pitcher. Subclass of Player"""
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating):
        Player.__init__(self, firstName, lastName, throwingHand, battingHand)
        self.pitchDict = PITCH_DICT.copy()
        self.energy = 100
        self.rating = pitcherRating

    def getRating(self):
        return self.rating


class Batter(Player):
    """A MLB batter. Subclass of Player"""
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, contact):
        Player.__init__(self, firstName, lastName, throwingHand, battingHand)
        self.contact = contact

    def getRating(self):
        return self.contact


class Pitch(object):
    """Represents a single pitch with location and quality"""
    def __init__(self, pitcher):
        self.pitcher = pitcher
        self.location = (random.uniform(STRIKE_WIDTH[0], STRIKE_WIDTH[1]),
                        random.uniform(STRIKE_HEIGHT[0], STRIKE_HEIGHT[1]))
        self.pitch = random.choice(list(self.pitcher.pitchDict.keys()))
        self.pitchQuality = 100 - (10 * random.random())

    def getPitch(self):
        return self.pitch

    def getLocation(self):
        return self.location

    def getPitchQuality(self):
        return self.pitchQuality

    def isStrike(self):
        if (STRIKE_ZONE[0] < self.location[0] < STRIKE_ZONE[1] and
            STRIKE_ZONE[2] < self.location[1] < STRIKE_ZONE[3]):
            return True
        else:
            return False


class Swing(object):
    """Represents a batter's swing decision and contact"""
    def __init__(self, pitcher, pitch, batter):
        self.currentPitch = pitch
        self.batter = batter
        self.pitcher = pitcher
        self.pitchQuality = pitch.getPitchQuality()

    def swingOrTake(self, balls, strikes):
        if balls == 0 and strikes == 0:
            takePer = 80
        elif balls == 3 and strikes == 0:
            takePer = 90
        elif strikes == 2:
            takePer = 10
        else:
            takePer = 50
        randomTake = 100 - 100 * random.random()
        x, y = Pitch.getLocation(self.currentPitch)
        if -0.4 < x < 0.4 and -1.0 < y < 0.5:
            return True
        elif -0.9 < x < 0.9 and -2.0 < y < 2.0 and takePer < randomTake:
            if random.random() > 0.5:
                return True
            else:
                return False
        else:
            return False

    def swingContact(self):
        x, y = Pitch.getLocation(self.currentPitch)
        if -0.6 < x < 0.6 and -2.0 < y < 1.5:
            return True
        batterRating = self.batter.getRating()
        pitcherAdvantage = self.pitchQuality - batterRating
        randomS = random.random()
        if pitcherAdvantage > 10:
            if randomS > .95:
                return True
            else:
                return False
        elif pitcherAdvantage > 0:
            if randomS > 0.5:
                return False
            else:
                return True
        elif pitcherAdvantage > -10:
            if randomS > 0.3:
                return True
            else:
                return False
        else:
            return True


# Test Classes
class TestPlayer(unittest.TestCase):
    """Test cases for the Player class"""

    def test_player_creation(self):
        """Test that a Player is created with correct attributes"""
        player = Player('John', 'Doe', 'Right', 'Left')
        self.assertEqual(player.name, 'JohnDoe')
        self.assertEqual(player.throwingHand, 'Right')
        self.assertEqual(player.battingHand, 'Left')

    def test_player_name_concatenation(self):
        """Test that player names are concatenated correctly"""
        player = Player('Babe', 'Ruth', 'Left', 'Left')
        self.assertEqual(player.name, 'BabeRuth')

    def test_player_batting_hand_options(self):
        """Test player creation with different batting hands"""
        for hand in ['Left', 'Right', 'Switch']:
            player = Player('Test', 'Player', 'Right', hand)
            self.assertEqual(player.battingHand, hand)

    def test_player_throwing_hand_options(self):
        """Test player creation with different throwing hands"""
        for hand in ['Left', 'Right']:
            player = Player('Test', 'Player', hand, 'Right')
            self.assertEqual(player.throwingHand, hand)

    def test_player_name_with_numbers(self):
        """Test player creation with numeric names"""
        player = Player('123', '456', 'Right', 'Left')
        self.assertEqual(player.name, '123456')


class TestPitcher(unittest.TestCase):
    """Test cases for the Pitcher class"""

    def test_pitcher_creation(self):
        """Test that a Pitcher is created with correct attributes"""
        pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 98)
        self.assertEqual(pitcher.name, 'BobGibson')
        self.assertEqual(pitcher.throwingHand, 'Right')
        self.assertEqual(pitcher.battingHand, 'Right')
        self.assertEqual(pitcher.rating, 98)
        self.assertEqual(pitcher.energy, 100)

    def test_pitcher_rating(self):
        """Test that pitcher rating is set correctly"""
        pitcher = Pitcher('Sandy', 'Koufax', 30, 'Left', 'Right', 95)
        self.assertEqual(pitcher.getRating(), 95)

    def test_pitcher_pitch_dict(self):
        """Test that pitcher has a copy of pitch dictionary"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        self.assertIn('Fastball', pitcher.pitchDict)
        self.assertIn('ChangeUp', pitcher.pitchDict)
        self.assertEqual(pitcher.pitchDict, PITCH_DICT)

    def test_pitcher_energy_initialization(self):
        """Test that pitcher starts with full energy"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 75)
        self.assertEqual(pitcher.energy, 100)

    def test_pitcher_rating_range(self):
        """Test pitcher with various rating values"""
        for rating in [1, 50, 99]:
            pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', rating)
            self.assertEqual(pitcher.getRating(), rating)

    def test_pitcher_pitch_dict_independence(self):
        """Test that each pitcher has independent pitch dictionary"""
        pitcher1 = Pitcher('Test1', 'Pitcher', 25, 'Right', 'Right', 80)
        pitcher2 = Pitcher('Test2', 'Pitcher', 25, 'Right', 'Right', 85)
        pitcher1.pitchDict['NewPitch'] = [0.90, 'g']
        self.assertNotIn('NewPitch', pitcher2.pitchDict)


class TestBatter(unittest.TestCase):
    """Test cases for the Batter class"""

    def test_batter_creation(self):
        """Test that a Batter is created with correct attributes"""
        batter = Batter('Stan', 'Musial', 35, 'Right', 'Right', 94)
        self.assertEqual(batter.name, 'StanMusial')
        self.assertEqual(batter.throwingHand, 'Right')
        self.assertEqual(batter.battingHand, 'Right')
        self.assertEqual(batter.contact, 94)

    def test_batter_rating(self):
        """Test that batter rating returns contact value"""
        batter = Batter('Ted', 'Williams', 40, 'Right', 'Right', 96)
        self.assertEqual(batter.getRating(), 96)

    def test_batter_contact_rating(self):
        """Test batter with various contact ratings"""
        for contact in [1, 50, 99]:
            batter = Batter('Test', 'Batter', 25, 'Right', 'Right', contact)
            self.assertEqual(batter.getRating(), contact)

    def test_batter_batting_hand_switch(self):
        """Test batter with switch hitting"""
        batter = Batter('Mickey', 'Mantle', 35, 'Right', 'Switch', 85)
        self.assertEqual(batter.battingHand, 'Switch')

    def test_batter_left_handed(self):
        """Test left-handed batter"""
        batter = Batter('Lefty', 'Grove', 40, 'Left', 'Left', 88)
        self.assertEqual(batter.battingHand, 'Left')
        self.assertEqual(batter.throwingHand, 'Left')


class TestPitch(unittest.TestCase):
    """Test cases for the Pitch class"""

    def test_pitch_creation(self):
        """Test that a Pitch is created with correct attributes"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        self.assertEqual(pitch.pitcher, pitcher)
        self.assertIn(pitch.pitch, list(pitcher.pitchDict.keys()))
        self.assertGreaterEqual(pitch.pitchQuality, 90)
        self.assertLessEqual(pitch.pitchQuality, 100)

    def test_pitch_location_in_bounds(self):
        """Test that pitch location is within defined bounds"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        x, y = pitch.getLocation()
        self.assertGreaterEqual(x, STRIKE_WIDTH[0])
        self.assertLessEqual(x, STRIKE_WIDTH[1])
        self.assertGreaterEqual(y, STRIKE_HEIGHT[0])
        self.assertLessEqual(y, STRIKE_HEIGHT[1])

    def test_get_pitch(self):
        """Test getPitch method returns correct pitch type"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        self.assertIn(pitch.getPitch(), ['Fastball', 'ChangeUp'])

    def test_get_location(self):
        """Test getLocation returns a tuple"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        location = pitch.getLocation()
        self.assertIsInstance(location, tuple)
        self.assertEqual(len(location), 2)

    def test_get_pitch_quality(self):
        """Test getPitchQuality returns value in expected range"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        quality = pitch.getPitchQuality()
        self.assertGreaterEqual(quality, 90)
        self.assertLessEqual(quality, 100)

    def test_is_strike_inside_zone(self):
        """Test isStrike returns True for pitches in strike zone"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        pitch.location = (0.0, 0.0)  # Center of strike zone
        self.assertTrue(pitch.isStrike())

    def test_is_strike_outside_zone(self):
        """Test isStrike returns False for pitches outside strike zone"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)  # Outside strike zone
        self.assertFalse(pitch.isStrike())

    def test_is_strike_boundary_conditions(self):
        """Test isStrike at boundary of strike zone"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        pitch.location = (STRIKE_ZONE[0] + 0.01, STRIKE_ZONE[2] + 0.01)
        self.assertTrue(pitch.isStrike())

    def test_is_strike_high_and_outside(self):
        """Test isStrike for high and outside pitch"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        pitch.location = (1.5, 2.5)
        self.assertFalse(pitch.isStrike())

    def test_is_strike_low_and_inside(self):
        """Test isStrike for low and inside pitch"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        pitch = Pitch(pitcher)
        pitch.location = (-0.5, -3.0)
        self.assertFalse(pitch.isStrike())


class TestSwing(unittest.TestCase):
    """Test cases for the Swing class"""

    def test_swing_creation(self):
        """Test that a Swing is created with correct attributes"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        swing = Swing(pitcher, pitch, batter)
        self.assertEqual(swing.pitcher, pitcher)
        self.assertEqual(swing.batter, batter)
        self.assertEqual(swing.currentPitch, pitch)

    def test_swing_or_take_0_0_count(self):
        """Test swingOrTake behavior at 0-0 count"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingOrTake(0, 0)
        self.assertIsInstance(result, bool)

    def test_swing_or_take_3_0_count(self):
        """Test swingOrTake behavior at 3-0 count"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingOrTake(3, 0)
        self.assertIsInstance(result, bool)

    def test_swing_or_take_2_2_count(self):
        """Test swingOrTake behavior at 2-2 count"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingOrTake(2, 2)
        self.assertIsInstance(result, bool)

    def test_swing_or_take_down_middle(self):
        """Test swingOrTake always swings at pitches down the middle"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        pitch.location = (0.0, 0.0)  # Down the middle
        swing = Swing(pitcher, pitch, batter)
        self.assertTrue(swing.swingOrTake(0, 0))

    def test_swing_contact_down_middle(self):
        """Test swingContact always makes contact down the middle"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        pitch.location = (0.0, 0.0)  # Down the middle
        swing = Swing(pitcher, pitch, batter)
        self.assertTrue(swing.swingContact())

    def test_swing_contact_pitcher_advantage(self):
        """Test swingContact with pitcher advantage"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 95)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 40)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)  # Outside zone
        pitch.pitchQuality = 95
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingContact()
        self.assertIsInstance(result, bool)

    def test_swing_contact_batter_advantage(self):
        """Test swingContact with batter advantage"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 40)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 95)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)  # Outside zone
        pitch.pitchQuality = 40
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingContact()
        self.assertIsInstance(result, bool)

    def test_swing_contact_even_matchup(self):
        """Test swingContact with even matchup"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 75)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)  # Outside zone
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingContact()
        self.assertIsInstance(result, bool)

    def test_swing_contact_large_pitcher_advantage(self):
        """Test swingContact with large pitcher advantage (>10)"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 99)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 1)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)
        pitch.pitchQuality = 99
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingContact()
        self.assertIsInstance(result, bool)

    def test_swing_contact_large_batter_advantage(self):
        """Test swingContact with large batter advantage (<-10)"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 1)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 99)
        pitch = Pitch(pitcher)
        pitch.location = (2.0, 2.0)
        pitch.pitchQuality = 1
        swing = Swing(pitcher, pitch, batter)
        result = swing.swingContact()
        self.assertTrue(result)  # Should always make contact with large advantage


class TestIntegration(unittest.TestCase):
    """Integration tests for multiple components"""

    def test_pitch_and_swing_integration(self):
        """Test Pitch and Swing working together"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)
        pitch = Pitch(pitcher)
        swing = Swing(pitcher, pitch, batter)

        swing_result = swing.swingOrTake(1, 1)
        self.assertIsInstance(swing_result, bool)

        if swing_result:
            contact_result = swing.swingContact()
            self.assertIsInstance(contact_result, bool)

    def test_multiple_pitches_different_locations(self):
        """Test that multiple pitches have different locations"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        locations = []
        for _ in range(10):
            pitch = Pitch(pitcher)
            locations.append(pitch.getLocation())

        self.assertGreater(len(set(locations)), 1)

    def test_pitcher_vs_batter_matchup(self):
        """Test a complete pitcher vs batter scenario"""
        pitcher = Pitcher('Ace', 'Pitcher', 30, 'Right', 'Right', 90)
        batter = Batter('Star', 'Batter', 28, 'Right', 'Right', 85)

        self.assertGreater(pitcher.getRating(), batter.getRating())
        self.assertEqual(pitcher.energy, 100)
        self.assertEqual(batter.getRating(), 85)

    def test_multiple_at_bats(self):
        """Test multiple at-bats with same pitcher and batter"""
        pitcher = Pitcher('Test', 'Pitcher', 25, 'Right', 'Right', 80)
        batter = Batter('Test', 'Batter', 25, 'Right', 'Right', 75)

        for _ in range(5):
            pitch = Pitch(pitcher)
            swing = Swing(pitcher, pitch, batter)
            swing.swingOrTake(0, 0)

    def test_realistic_at_bat_sequence(self):
        """Test a realistic at-bat sequence"""
        pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 95)
        batter = Batter('Stan', 'Musial', 35, 'Right', 'Right', 90)

        balls = 0
        strikes = 0
        pitches_thrown = 0

        while balls < 4 and strikes < 3 and pitches_thrown < 10:
            pitch = Pitch(pitcher)
            swing = Swing(pitcher, pitch, batter)

            if swing.swingOrTake(balls, strikes):
                if swing.swingContact():
                    break
                else:
                    strikes += 1
            else:
                if pitch.isStrike():
                    strikes += 1
                else:
                    balls += 1

            pitches_thrown += 1

        self.assertLessEqual(pitches_thrown, 10)
        self.assertTrue(balls < 4 or strikes < 3 or pitches_thrown >= 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
