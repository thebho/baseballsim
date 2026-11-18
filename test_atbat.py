import unittest
import random
import sys
from unittest.mock import patch

# Mock pylab before importing atbat
sys.modules['pylab'] = __import__('unittest.mock').mock.MagicMock()

from atbat import (
    Player, Pitcher, Batter, Pitch, Swing, 
    STRIKE_ZONE, STRIKE_WIDTH, STRIKE_HEIGHT, PITCH_DICT
)


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class"""
    
    def test_player_creation(self):
        """Test that a player can be created with correct attributes"""
        player = Player('John', 'Doe', 'Right', 'Left')
        self.assertEqual(player.name, 'JohnDoe')
        self.assertEqual(player.throwingHand, 'Right')
        self.assertEqual(player.battingHand, 'Left')
    
    def test_player_name_concatenation(self):
        """Test that player names are properly concatenated"""
        player = Player('Bob', 'Gibson', 'Right', 'Right')
        self.assertEqual(player.name, 'BobGibson')


class TestPitcher(unittest.TestCase):
    """Test cases for the Pitcher class"""
    
    def setUp(self):
        """Create a pitcher for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)
    
    def test_pitcher_creation(self):
        """Test that a pitcher is created with correct attributes"""
        self.assertEqual(self.pitcher.name, 'BobGibson')
        self.assertEqual(self.pitcher.rating, 98)
        self.assertEqual(self.pitcher.energy, 100)
        self.assertEqual(self.pitcher.throwingHand, 'Right')
        self.assertEqual(self.pitcher.battingHand, 'Right')
    
    def test_pitcher_rating(self):
        """Test that pitcher rating is returned correctly"""
        self.assertEqual(self.pitcher.getRating(), 98)
    
    def test_pitcher_pitch_dict(self):
        """Test that pitcher has a copy of the pitch dictionary"""
        self.assertIn('Fastball', self.pitcher.pitchDict)
        self.assertIn('ChangeUp', self.pitcher.pitchDict)
        # Verify it's a copy, not a reference
        self.assertIsNot(self.pitcher.pitchDict, PITCH_DICT)


class TestBatter(unittest.TestCase):
    """Test cases for the Batter class"""
    
    def setUp(self):
        """Create a batter for testing"""
        self.batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)
    
    def test_batter_creation(self):
        """Test that a batter is created with correct attributes"""
        self.assertEqual(self.batter.name, 'StanMusial')
        self.assertEqual(self.batter.contact, 94)
        self.assertEqual(self.batter.throwingHand, 'Right')
        self.assertEqual(self.batter.battingHand, 'Right')
    
    def test_batter_rating(self):
        """Test that batter rating (contact) is returned correctly"""
        self.assertEqual(self.batter.getRating(), 94)
    
    def test_batter_low_contact(self):
        """Test creating a batter with low contact rating"""
        bad_batter = Batter('Bad', 'Batter', 40, 'Left', 'Left', 40)
        self.assertEqual(bad_batter.getRating(), 40)


class TestPitch(unittest.TestCase):
    """Test cases for the Pitch class"""
    
    def setUp(self):
        """Create a pitcher and pitch for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)
        random.seed(42)  # For reproducible tests
    
    def test_pitch_creation(self):
        """Test that a pitch is created with valid attributes"""
        pitch = Pitch(self.pitcher)
        self.assertIsNotNone(pitch.pitch)
        self.assertIn(pitch.pitch, self.pitcher.pitchDict.keys())
    
    def test_pitch_location_in_bounds(self):
        """Test that pitch location is within expected bounds"""
        pitch = Pitch(self.pitcher)
        x, y = pitch.getLocation()
        self.assertGreaterEqual(x, STRIKE_WIDTH[0])
        self.assertLessEqual(x, STRIKE_WIDTH[1])
        self.assertGreaterEqual(y, STRIKE_HEIGHT[0])
        self.assertLessEqual(y, STRIKE_HEIGHT[1])
    
    def test_pitch_quality_in_range(self):
        """Test that pitch quality is in expected range"""
        pitch = Pitch(self.pitcher)
        quality = pitch.getPitchQuality()
        self.assertGreaterEqual(quality, 90)
        self.assertLessEqual(quality, 100)
    
    def test_get_pitch(self):
        """Test getPitch method"""
        pitch = Pitch(self.pitcher)
        self.assertEqual(pitch.getPitch(), pitch.pitch)
    
    def test_is_strike_center(self):
        """Test that a pitch in the center of the zone is a strike"""
        pitch = Pitch(self.pitcher)
        # Manually set location to center of strike zone
        pitch.location = (0.0, 0.0)
        self.assertTrue(pitch.isStrike())
    
    def test_is_strike_outside_zone(self):
        """Test that a pitch outside the zone is not a strike"""
        pitch = Pitch(self.pitcher)
        # Manually set location outside strike zone
        pitch.location = (2.0, 2.0)
        self.assertFalse(pitch.isStrike())
    
    def test_is_strike_boundary(self):
        """Test strike zone boundaries"""
        pitch = Pitch(self.pitcher)
        # Test left boundary
        pitch.location = (STRIKE_ZONE[0] + 0.01, 0.0)
        self.assertTrue(pitch.isStrike())
        
        # Test right boundary
        pitch.location = (STRIKE_ZONE[1] - 0.01, 0.0)
        self.assertTrue(pitch.isStrike())


class TestSwing(unittest.TestCase):
    """Test cases for the Swing class"""
    
    def setUp(self):
        """Create pitcher, batter, and pitch for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)
        self.batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)
        random.seed(42)
        self.pitch = Pitch(self.pitcher)
        self.swing = Swing(self.pitcher, self.pitch, self.batter)
    
    def test_swing_creation(self):
        """Test that a swing is created with correct attributes"""
        self.assertEqual(self.swing.batter, self.batter)
        self.assertEqual(self.swing.pitcher, self.pitcher)
        self.assertEqual(self.swing.currentPitch, self.pitch)
    
    def test_swing_or_take_returns_boolean(self):
        """Test that swingOrTake returns a boolean"""
        result = self.swing.swingOrTake(0, 0)
        self.assertIsInstance(result, bool)
    
    def test_swing_contact_returns_boolean(self):
        """Test that swingContact returns a boolean"""
        result = self.swing.swingContact()
        self.assertIsInstance(result, bool)
    
    def test_swing_or_take_different_counts(self):
        """Test swingOrTake with different ball/strike counts"""
        # Test 0-0 count
        result_0_0 = self.swing.swingOrTake(0, 0)
        self.assertIsInstance(result_0_0, bool)
        
        # Test 3-0 count
        result_3_0 = self.swing.swingOrTake(3, 0)
        self.assertIsInstance(result_3_0, bool)
        
        # Test 0-2 count
        result_0_2 = self.swing.swingOrTake(0, 2)
        self.assertIsInstance(result_0_2, bool)
    
    def test_swing_contact_down_middle(self):
        """Test that contact is made on pitches down the middle"""
        self.pitch.location = (0.0, 0.0)  # Center of strike zone
        result = self.swing.swingContact()
        self.assertTrue(result)  # Should make contact down the middle
    
    def test_swing_contact_with_high_batter_rating(self):
        """Test swing contact with a high-rated batter"""
        good_batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 95)
        swing = Swing(self.pitcher, self.pitch, good_batter)
        result = swing.swingContact()
        self.assertIsInstance(result, bool)


class TestIntegration(unittest.TestCase):
    """Integration tests for the baseball simulation"""
    
    def setUp(self):
        """Create players for integration testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98)
        self.batter = Batter('Stan', 'Musial', 20, 'Right', 'Right', 94)
        random.seed(42)
    
    def test_pitch_and_swing_sequence(self):
        """Test a sequence of pitches and swings"""
        for _ in range(5):
            pitch = Pitch(self.pitcher)
            swing = Swing(self.pitcher, pitch, self.batter)
            
            # Test that we can get swing decision
            swing_decision = swing.swingOrTake(0, 0)
            self.assertIsInstance(swing_decision, bool)
            
            # If swinging, test contact decision
            if swing_decision:
                contact = swing.swingContact()
                self.assertIsInstance(contact, bool)
    
    def test_multiple_pitchers_and_batters(self):
        """Test with different pitcher and batter combinations"""
        pitchers = [
            Pitcher('Bob', 'Gibson', 20, 'Right', 'Right', 98),
            Pitcher('Sandy', 'Koufax', 25, 'Left', 'Right', 96),
        ]
        batters = [
            Batter('Stan', 'Musial', 20, 'Right', 'Right', 94),
            Batter('Bad', 'Batter', 40, 'Left', 'Left', 40),
        ]
        
        for pitcher in pitchers:
            for batter in batters:
                pitch = Pitch(pitcher)
                swing = Swing(pitcher, pitch, batter)
                self.assertIsNotNone(swing)


if __name__ == '__main__':
    unittest.main()
