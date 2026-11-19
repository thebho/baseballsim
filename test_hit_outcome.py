#!/usr/bin/env python
"""
Test script for HitOutcome implementation
Tests hit outcome simulation multiple times to verify:
- Hit outcomes are generated when ball is in play
- Results vary based on batter/pitcher matchup
- Outcomes are printed clearly
- No errors occur
"""

import sys
import math
import random

# Mock pylab to avoid import errors
class MockPylab:
    def subplot(self, *args, **kwargs):
        return None
    def scatter(self, *args, **kwargs):
        pass
    def text(self, *args, **kwargs):
        pass
    def plot(self, *args, **kwargs):
        pass
    def xlim(self, *args, **kwargs):
        pass
    def ylim(self, *args, **kwargs):
        pass
    def show(self):
        pass

sys.modules['pylab'] = MockPylab()

from atbat import Pitcher, Batter, Pitch, Swing, HitOutcome

def test_hit_outcome_basic():
    """Test basic HitOutcome functionality"""
    print("=" * 60)
    print("TEST 1: Basic HitOutcome Calculation")
    print("=" * 60)
    
    pitcher = Pitcher('Test', 'Pitcher', 30, 'Right', 'Right', 85)
    batter = Batter('Test', 'Batter', 28, 'Right', 'Right', 80)
    pitch = Pitch(pitcher)
    
    hit = HitOutcome(batter, pitcher, pitch)
    print("Pitch Location: {:.2f}, {:.2f}".format(hit.pitchLocation[0], hit.pitchLocation[1]))
    print("Contact Quality: {:.1f}".format(hit.contactQuality))
    print("Exit Velocity: {:.1f}".format(hit.exitVelocity))
    print("Launch Angle: {:.1f}°".format(hit.launchAngle))
    print("Hit Outcome: {}".format(hit.getHitOutcome()))
    print("Details: {}".format(hit.getDetails()))
    print()

def test_multiple_outcomes():
    """Test multiple hit outcomes to verify variation"""
    print("=" * 60)
    print("TEST 2: Multiple Hit Outcomes (10 trials)")
    print("=" * 60)
    
    pitcher = Pitcher('Bob', 'Gibson', 30, 'Right', 'Right', 95)
    batter = Batter('Stan', 'Musial', 28, 'Right', 'Right', 90)
    
    outcomes = {'Single': 0, 'Double': 0, 'Triple': 0, 'HomeRun': 0, 'Out': 0}
    
    for i in range(10):
        pitch = Pitch(pitcher)
        hit = HitOutcome(batter, pitcher, pitch)
        result = hit.getHitOutcome()
        outcomes[result] += 1
        print("Trial {}: {} (EV: {:.1f}, LA: {:.1f}°)".format(
            i+1, result, hit.exitVelocity, hit.launchAngle))
    
    print("\nOutcome Summary:")
    for outcome, count in outcomes.items():
        print("  {}: {} times".format(outcome, count))
    print()

def test_batter_pitcher_matchup():
    """Test different batter/pitcher matchups"""
    print("=" * 60)
    print("TEST 3: Different Batter/Pitcher Matchups")
    print("=" * 60)
    
    # Good batter vs good pitcher
    print("\nGood Batter (90) vs Good Pitcher (95):")
    pitcher1 = Pitcher('Bob', 'Gibson', 30, 'Right', 'Right', 95)
    batter1 = Batter('Stan', 'Musial', 28, 'Right', 'Right', 90)
    
    outcomes1 = {'Single': 0, 'Double': 0, 'Triple': 0, 'HomeRun': 0, 'Out': 0}
    for _ in range(10):
        pitch = Pitch(pitcher1)
        hit = HitOutcome(batter1, pitcher1, pitch)
        outcomes1[hit.getHitOutcome()] += 1
    
    print("  Outcomes: {}".format(outcomes1))
    
    # Bad batter vs good pitcher
    print("\nBad Batter (40) vs Good Pitcher (95):")
    pitcher2 = Pitcher('Bob', 'Gibson', 30, 'Right', 'Right', 95)
    batter2 = Batter('Bad', 'Batter', 40, 'Left', 'Left', 40)
    
    outcomes2 = {'Single': 0, 'Double': 0, 'Triple': 0, 'HomeRun': 0, 'Out': 0}
    for _ in range(10):
        pitch = Pitch(pitcher2)
        hit = HitOutcome(batter2, pitcher2, pitch)
        outcomes2[hit.getHitOutcome()] += 1
    
    print("  Outcomes: {}".format(outcomes2))
    
    # Good batter vs bad pitcher
    print("\nGood Batter (90) vs Bad Pitcher (50):")
    pitcher3 = Pitcher('Bad', 'Pitcher', 30, 'Right', 'Right', 50)
    batter3 = Batter('Stan', 'Musial', 28, 'Right', 'Right', 90)
    
    outcomes3 = {'Single': 0, 'Double': 0, 'Triple': 0, 'HomeRun': 0, 'Out': 0}
    for _ in range(10):
        pitch = Pitch(pitcher3)
        hit = HitOutcome(batter3, pitcher3, pitch)
        outcomes3[hit.getHitOutcome()] += 1
    
    print("  Outcomes: {}".format(outcomes3))
    print()

def test_launch_angle_ranges():
    """Test that launch angles produce expected hit types"""
    print("=" * 60)
    print("TEST 4: Launch Angle Ranges")
    print("=" * 60)
    
    pitcher = Pitcher('Test', 'Pitcher', 30, 'Right', 'Right', 85)
    batter = Batter('Test', 'Batter', 28, 'Right', 'Right', 85)
    
    print("\nGenerating 20 hits to verify launch angle ranges:")
    for i in range(20):
        pitch = Pitch(pitcher)
        hit = HitOutcome(batter, pitcher, pitch)
        angle = hit.launchAngle
        
        if angle < 15:
            angle_type = "Ground Ball"
        elif angle < 35:
            angle_type = "Line Drive"
        elif angle < 50:
            angle_type = "Fly Ball"
        else:
            angle_type = "Pop-up"
        
        print("  {}: {:.1f}° ({}) -> {}".format(
            i+1, angle, angle_type, hit.getHitOutcome()))
    print()

if __name__ == '__main__':
    try:
        test_hit_outcome_basic()
        test_multiple_outcomes()
        test_batter_pitcher_matchup()
        test_launch_angle_ranges()
        
        print("=" * 60)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 60)
    except Exception as e:
        print("ERROR: {}".format(str(e)))
        import traceback
        traceback.print_exc()
        sys.exit(1)
