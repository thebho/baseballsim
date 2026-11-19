import unittest
import random
from atbat import (
    Player, Pitcher, Batter, Pitch, Swing,
    PITCH_DICT, STRIKE_ZONE, STRIKE_WIDTH, STRIKE_HEIGHT
)


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
    
    def test_player_throwing_hand_options(self):
        """Test that throwing hand can be Left or Right"""
        player_left = Player('Test', 'Left', 'Left', 'Right')
        player_right = Player('Test', 'Right', 'Right', 'Left')
        self.assertIn(player_left.throwingHand, ['Left', 'Right'])
        self.assertIn(player_right.throwingHand, ['Left', 'Right'])
    
    def test_player_batting_hand_options(self):
        """Test that batting hand can be Left, Right, or Switch"""
        for hand in ['Left', 'Right', 'Switch']:
            player = Player('Test', 'Player', 'Right', hand)
            self.assertEqual(player.battingHand, hand)


class TestPitcher(unittest.TestCase):
    """Test cases for the Pitcher class"""
    
    def setUp(self):
        """Create a pitcher for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 98)
    
    def test_pitcher_creation(self):
        """Test that a Pitcher is created with correct attributes"""
        self.assertEqual(self.pitcher.name, 'BobGibson')
        self.assertEqual(self.pitcher.rating, 98)
        self.assertEqual(self.pitcher.energy, 100)
        self.assertEqual(self.pitcher.throwingHand, 'Right')
    
    def test_pitcher_inherits_from_player(self):
        """Test that Pitcher inherits from Player"""
        self.assertIsInstance(self.pitcher, Player)
    
    def test_pitcher_rating_range(self):
        """Test pitcher with various ratings"""
        for rating in [1, 50, 99]:
            pitcher = Pitcher('Test', 'Pitcher', 30, 'Right', 'Right', rating)
            self.assertEqual(pitcher.rating, rating)
    
    def test_pitcher_get_rating(self):
        """Test getRating method"""
        self.assertEqual(self.pitcher.getRating(), 98)
    
    def test_pitcher_has_pitch_dict(self):
        """Test that pitcher has a copy of PITCH_DICT"""
        self.assertIsNotNone(self.pitcher.pitchDict)
        self.assertIn('Fastball', self.pitcher.pitchDict)
        self.assertIn('ChangeUp', self.pitcher.pitchDict)
    
    def test_pitcher_pitch_dict_is_copy(self):
        """Test that pitcher's pitchDict is a copy, not a reference"""
        original_dict = PITCH_DICT.copy()
        self.pitcher.pitchDict['NewPitch'] = [0.90, 'g']
        self.assertNotIn('NewPitch', PITCH_DICT)


class TestBatter(unittest.TestCase):
    """Test cases for the Batter class"""
    
    def setUp(self):
        """Create a batter for testing"""
        self.batter = Batter('Stan', 'Musial', 35, 'Right', 'Right', 94)
    
    def test_batter_creation(self):
        """Test that a Batter is created with correct attributes"""
        self.assertEqual(self.batter.name, 'StanMusial')
        self.assertEqual(self.batter.contact, 94)
        self.assertEqual(self.batter.battingHand, 'Right')
    
    def test_batter_inherits_from_player(self):
        """Test that Batter inherits from Player"""
        self.assertIsInstance(self.batter, Player)
    
    def test_batter_contact_range(self):
        """Test batter with various contact ratings"""
        for contact in [1, 50, 99]:
            batter = Batter('Test', 'Batter', 30, 'Right', 'Right', contact)
            self.assertEqual(batter.contact, contact)
    
    def test_batter_get_rating(self):
        """Test getRating method returns contact"""
        self.assertEqual(self.batter.getRating(), 94)
    
    def test_bad_batter_creation(self):
        """Test creation of a poor batter"""
        bad_batter = Batter('Bad', 'Batter', 40, 'Left', 'Left', 40)
        self.assertEqual(bad_batter.contact, 40)
        self.assertEqual(bad_batter.getRating(), 40)


class TestPitch(unittest.TestCase):
    """Test cases for the Pitch class"""
    
    def setUp(self):
        """Create a pitcher and pitch for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 98)
        random.seed(42)  # For reproducible tests
    
    def test_pitch_creation(self):
        """Test that a Pitch is created with required attributes"""
        pitch = Pitch(self.pitcher)
        self.assertIsNotNone(pitch.pitcher)
        self.assertIsNotNone(pitch.location)
        self.assertIsNotNone(pitch.pitch)
        self.assertIsNotNone(pitch.pitchQuality)
    
    def test_pitch_location_within_bounds(self):
        """Test that pitch location is within strike width and height"""
        for _ in range(10):
            pitch = Pitch(self.pitcher)
            x, y = pitch.location
            self.assertGreaterEqual(x, STRIKE_WIDTH[0])
            self.assertLessEqual(x, STRIKE_WIDTH[1])
            self.assertGreaterEqual(y, STRIKE_HEIGHT[0])
            self.assertLessEqual(y, STRIKE_HEIGHT[1])
    
    def test_pitch_type_valid(self):
        """Test that pitch type is one of the available pitches"""
        for _ in range(10):
            pitch = Pitch(self.pitcher)
            self.assertIn(pitch.pitch, self.pitcher.pitchDict.keys())
    
    def test_pitch_quality_range(self):
        """Test that pitch quality is between 90 and 100"""
        for _ in range(10):
            pitch = Pitch(self.pitcher)
            self.assertGreaterEqual(pitch.pitchQuality, 90)
            self.assertLessEqual(pitch.pitchQuality, 100)
    
    def test_get_pitch(self):
        """Test getPitch method"""
        pitch = Pitch(self.pitcher)
        self.assertEqual(pitch.getPitch(), pitch.pitch)
    
    def test_get_location(self):
        """Test getLocation method"""
        pitch = Pitch(self.pitcher)
        self.assertEqual(pitch.getLocation(), pitch.location)
    
    def test_get_pitch_quality(self):
        """Test getPitchQuality method"""
        pitch = Pitch(self.pitcher)
        self.assertEqual(pitch.getPitchQuality(), pitch.pitchQuality)
    
    def test_is_strike_center(self):
        """Test isStrike for pitch down the middle"""
        pitch = Pitch(self.pitcher)
        pitch.location = (0.0, 0.0)  # Center of strike zone
        self.assertTrue(pitch.isStrike())
    
    def test_is_strike_edges(self):
        """Test isStrike for pitches at zone edges"""
        pitch = Pitch(self.pitcher)
        # Test corners of strike zone
        test_locations = [
            (STRIKE_ZONE[0] + 0.01, STRIKE_ZONE[2] + 0.01),  # Lower left
            (STRIKE_ZONE[1] - 0.01, STRIKE_ZONE[3] - 0.01),  # Upper right
        ]
        for loc in test_locations:
            pitch.location = loc
            self.assertTrue(pitch.isStrike())
    
    def test_is_strike_outside_zone(self):
        """Test isStrike for pitches outside strike zone"""
        pitch = Pitch(self.pitcher)
        # Test locations outside strike zone
        test_locations = [
            (-2.0, 0.0),  # Far left
            (2.0, 0.0),   # Far right
            (0.0, -3.0),  # Below zone
            (0.0, 2.0),   # Above zone
        ]
        for loc in test_locations:
            pitch.location = loc
            self.assertFalse(pitch.isStrike())
    
    def test_is_strike_boundary_conditions(self):
        """Test isStrike at exact boundaries"""
        pitch = Pitch(self.pitcher)
        # Just outside boundaries should be False
        pitch.location = (STRIKE_ZONE[0] - 0.01, 0.0)
        self.assertFalse(pitch.isStrike())
        
        pitch.location = (STRIKE_ZONE[1] + 0.01, 0.0)
        self.assertFalse(pitch.isStrike())


class TestSwing(unittest.TestCase):
    """Test cases for the Swing class"""
    
    def setUp(self):
        """Create pitcher, batter, and pitch for testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 98)
        self.batter = Batter('Stan', 'Musial', 35, 'Right', 'Right', 94)
        self.pitch = Pitch(self.pitcher)
        self.swing = Swing(self.pitcher, self.pitch, self.batter)
    
    def test_swing_creation(self):
        """Test that a Swing is created with correct attributes"""
        self.assertEqual(self.swing.pitcher, self.pitcher)
        self.assertEqual(self.swing.batter, self.batter)
        self.assertEqual(self.swing.currentPitch, self.pitch)
    
    def test_swing_or_take_0_0_count(self):
        """Test swingOrTake at 0-0 count (should mostly take)"""
        self.pitch.location = (0.0, 0.0)  # Middle of zone
        # At 0-0, batter should swing at middle pitches
        result = self.swing.swingOrTake(0, 0)
        self.assertIsInstance(result, bool)
    
    def test_swing_or_take_3_0_count(self):
        """Test swingOrTake at 3-0 count (should mostly take)"""
        self.pitch.location = (0.0, 0.0)
        result = self.swing.swingOrTake(3, 0)
        self.assertIsInstance(result, bool)
    
    def test_swing_or_take_0_2_count(self):
        """Test swingOrTake at 0-2 count (should mostly swing)"""
        self.pitch.location = (0.0, 0.0)
        result = self.swing.swingOrTake(0, 2)
        self.assertIsInstance(result, bool)
    
    def test_swing_or_take_middle_pitch(self):
        """Test that middle pitches are swung at"""
        self.pitch.location = (0.0, 0.0)  # Dead center
        result = self.swing.swingOrTake(1, 1)
        self.assertTrue(result)  # Should swing at middle pitch
    
    def test_swing_contact_middle_pitch(self):
        """Test swingContact for middle pitch (should make contact)"""
        self.pitch.location = (0.0, 0.0)  # Dead center
        result = self.swing.swingContact()
        self.assertTrue(result)  # Should make contact on middle pitch
    
    def test_swing_contact_returns_bool(self):
        """Test that swingContact returns a boolean"""
        result = self.swing.swingContact()
        self.assertIsInstance(result, bool)
    
    def test_swing_contact_pitcher_advantage(self):
        """Test swingContact with pitcher advantage"""
        # High pitch quality (pitcher advantage)
        self.swing.pitchQuality = 95
        self.batter.contact = 40
        # Pitcher has significant advantage
        result = self.swing.swingContact()
        self.assertIsInstance(result, bool)
    
    def test_swing_contact_batter_advantage(self):
        """Test swingContact with batter advantage"""
        # Low pitch quality (batter advantage)
        self.swing.pitchQuality = 40
        self.batter.contact = 95
        # Batter has significant advantage
        result = self.swing.swingContact()
        self.assertIsInstance(result, bool)
    
    def test_swing_contact_even_matchup(self):
        """Test swingContact with even matchup"""
        self.swing.pitchQuality = 70
        self.batter.contact = 70
        result = self.swing.swingContact()
        self.assertIsInstance(result, bool)


class TestStrikeZone(unittest.TestCase):
    """Test cases for strike zone logic"""
    
    def test_strike_zone_constants(self):
        """Test that strike zone constants are defined"""
        self.assertEqual(len(STRIKE_ZONE), 4)
        self.assertLess(STRIKE_ZONE[0], STRIKE_ZONE[1])  # x bounds
        self.assertLess(STRIKE_ZONE[2], STRIKE_ZONE[3])  # y bounds
    
    def test_strike_width_constants(self):
        """Test that strike width constants are defined"""
        self.assertEqual(len(STRIKE_WIDTH), 2)
        self.assertLess(STRIKE_WIDTH[0], STRIKE_WIDTH[1])
    
    def test_strike_height_constants(self):
        """Test that strike height constants are defined"""
        self.assertEqual(len(STRIKE_HEIGHT), 2)
        self.assertLess(STRIKE_HEIGHT[0], STRIKE_HEIGHT[1])


class TestIntegration(unittest.TestCase):
    """Integration tests for the baseball simulation"""
    
    def setUp(self):
        """Create players for integration testing"""
        self.pitcher = Pitcher('Bob', 'Gibson', 35, 'Right', 'Right', 98)
        self.batter = Batter('Stan', 'Musial', 35, 'Right', 'Right', 94)
        self.bad_batter = Batter('Bad', 'Batter', 40, 'Left', 'Left', 40)
    
    def test_pitch_and_swing_sequence(self):
        """Test a sequence of pitch and swing"""
        pitch = Pitch(self.pitcher)
        swing = Swing(self.pitcher, pitch, self.batter)
        
        # Should be able to determine swing/take
        swing_result = swing.swingOrTake(0, 0)
        self.assertIsInstance(swing_result, bool)
        
        # If swinging, should be able to determine contact
        if swing_result:
            contact_result = swing.swingContact()
            self.assertIsInstance(contact_result, bool)
    
    def test_multiple_pitches(self):
        """Test throwing multiple pitches"""
        pitches = []
        for _ in range(5):
            pitch = Pitch(self.pitcher)
            pitches.append(pitch)
            self.assertIsNotNone(pitch.location)
            self.assertIsNotNone(pitch.pitch)
    
    def test_good_batter_vs_bad_pitcher(self):
        """Test good batter against bad pitcher"""
        bad_pitcher = Pitcher('Bad', 'Pitcher', 30, 'Right', 'Right', 40)
        good_batter = Batter('Good', 'Batter', 30, 'Right', 'Right', 95)
        
        pitch = Pitch(bad_pitcher)
        swing = Swing(bad_pitcher, pitch, good_batter)
        
        self.assertIsNotNone(swing)
        self.assertEqual(swing.batter.getRating(), 95)
        self.assertEqual(swing.pitcher.getRating(), 40)


if __name__ == '__main__':
    unittest.main()
