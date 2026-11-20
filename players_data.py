"""
players_data.py - Contains 100 fictional baseball players (40 pitchers, 60 batters)
"""

from atbat import Pitcher, Batter

# Teams
TEAMS = [
    "River Cats",
    "Iron Wolves",
    "Coastal Kings",
    "Desert Hawks",
    "Northside Thunder",
    "Bay Breakers",
    "Summit Eagles",
    "Lakewood Aces"
]

# Pitcher positions
PITCHER_POSITIONS = ["SP", "RP"]

# Batter positions
BATTER_POSITIONS = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "DH"]

# ============================================================================
# PITCHERS (40 total)
# ============================================================================

PITCHERS = [
    # Low skill pitchers (30-50)
    Pitcher("Marcus", "Webb", "Right", "Right", 26, "6'3\"", 210, "SP", "River Cats", 1, 3, 38, 42, 35, 40, 2, 5, 5.12),
    Pitcher("Derek", "Paulson", "Left", "Left", 28, "6'1\"", 195, "RP", "Iron Wolves", 2, 4, 35, 38, 40, 36, 1, 3, 5.67),
    Pitcher("Kevin", "Hartley", "Right", "Right", 31, "6'4\"", 225, "SP", "Coastal Kings", 3, 8, 42, 45, 38, 41, 5, 8, 4.89),
    Pitcher("Jason", "Brennan", "Left", "Right", 24, "6'0\"", 185, "RP", "Desert Hawks", 4, 2, 40, 39, 42, 37, 0, 2, 6.01),
    Pitcher("Tyler", "Simmons", "Right", "Left", 29, "6'2\"", 205, "SP", "Northside Thunder", 5, 5, 38, 41, 36, 39, 3, 6, 5.34),
    Pitcher("Brandon", "Cole", "Right", "Right", 27, "6'3\"", 215, "RP", "Bay Breakers", 6, 3, 36, 40, 39, 38, 1, 4, 5.78),
    Pitcher("Chris", "Mendez", "Left", "Left", 32, "6'1\"", 200, "SP", "Summit Eagles", 7, 9, 41, 43, 37, 42, 6, 9, 4.95),
    Pitcher("Ryan", "Foster", "Right", "Right", 25, "6'2\"", 208, "RP", "Lakewood Aces", 8, 2, 39, 38, 41, 36, 0, 3, 5.89),
    Pitcher("David", "Nichols", "Left", "Right", 30, "6'0\"", 190, "SP", "River Cats", 9, 6, 43, 44, 40, 43, 4, 7, 5.01),
    Pitcher("Eric", "Ramirez", "Right", "Left", 26, "6'4\"", 220, "RP", "Iron Wolves", 10, 3, 37, 39, 38, 35, 1, 5, 5.56),
    Pitcher("Scott", "Harrison", "Right", "Right", 28, "6'2\"", 212, "SP", "Coastal Kings", 11, 4, 40, 42, 39, 40, 2, 6, 5.23),
    Pitcher("Michael", "Torres", "Left", "Left", 33, "6'1\"", 198, "RP", "Desert Hawks", 12, 10, 44, 46, 41, 44, 7, 10, 4.78),
    Pitcher("Anthony", "Gomez", "Right", "Right", 27, "6'3\"", 218, "SP", "Northside Thunder", 13, 5, 39, 41, 37, 38, 3, 5, 5.45),
    
    # Mid skill pitchers (51-74)
    Pitcher("James", "Mitchell", "Right", "Right", 29, "6'2\"", 210, "SP", "Bay Breakers", 14, 6, 62, 65, 68, 64, 12, 8, 3.45),
    Pitcher("Robert", "Sullivan", "Left", "Left", 31, "6'1\"", 205, "RP", "Summit Eagles", 15, 8, 58, 61, 64, 59, 9, 11, 3.78),
    Pitcher("William", "Chen", "Right", "Right", 26, "6'3\"", 215, "SP", "Lakewood Aces", 16, 4, 65, 68, 71, 66, 14, 9, 3.12),
    Pitcher("Joseph", "Anderson", "Left", "Right", 30, "6'0\"", 195, "RP", "River Cats", 17, 7, 61, 63, 67, 62, 11, 10, 3.56),
    Pitcher("Charles", "Davis", "Right", "Left", 28, "6'4\"", 225, "SP", "Iron Wolves", 18, 5, 64, 66, 69, 65, 13, 7, 3.34),
    Pitcher("Richard", "Martinez", "Right", "Right", 32, "6'2\"", 212, "RP", "Coastal Kings", 19, 9, 59, 62, 65, 60, 10, 12, 3.67),
    Pitcher("Thomas", "Jackson", "Left", "Left", 27, "6'1\"", 200, "SP", "Desert Hawks", 20, 5, 63, 64, 68, 63, 12, 8, 3.41),
    Pitcher("Daniel", "White", "Right", "Right", 29, "6'3\"", 220, "RP", "Northside Thunder", 21, 6, 60, 59, 66, 61, 10, 9, 3.72),
    Pitcher("Matthew", "Brown", "Left", "Right", 31, "6'0\"", 190, "SP", "Bay Breakers", 22, 8, 66, 67, 70, 67, 15, 10, 3.23),
    Pitcher("Mark", "Johnson", "Right", "Left", 26, "6'2\"", 208, "RP", "Summit Eagles", 23, 4, 57, 60, 63, 58, 8, 10, 3.89),
    Pitcher("Donald", "Williams", "Right", "Right", 30, "6'4\"", 225, "SP", "Lakewood Aces", 24, 7, 64, 65, 68, 64, 13, 9, 3.38),
    Pitcher("Steven", "Jones", "Left", "Left", 28, "6'1\"", 205, "RP", "River Cats", 25, 5, 61, 62, 66, 61, 11, 8, 3.54),
    Pitcher("Paul", "Garcia", "Right", "Right", 32, "6'3\"", 218, "SP", "Iron Wolves", 26, 9, 65, 66, 69, 65, 14, 11, 3.29),
    Pitcher("Andrew", "Rodriguez", "Left", "Right", 27, "6'0\"", 195, "RP", "Coastal Kings", 27, 5, 59, 61, 64, 60, 9, 9, 3.65),
    
    # High skill pitchers (75-99)
    Pitcher("Christopher", "Lee", "Right", "Right", 31, "6'2\"", 210, "SP", "Desert Hawks", 28, 10, 88, 91, 94, 89, 28, 12, 2.34),
    Pitcher("Kenneth", "Taylor", "Left", "Left", 29, "6'1\"", 205, "RP", "Northside Thunder", 29, 7, 85, 88, 91, 86, 24, 10, 2.67),
    Pitcher("Edward", "Thomas", "Right", "Right", 33, "6'4\"", 225, "SP", "Bay Breakers", 30, 12, 92, 94, 96, 93, 32, 14, 2.12),
    Pitcher("Ronald", "Moore", "Left", "Right", 28, "6'0\"", 190, "RP", "Summit Eagles", 31, 6, 82, 85, 88, 83, 21, 8, 2.89),
    Pitcher("George", "Clark", "Right", "Left", 30, "6'3\"", 220, "SP", "Lakewood Aces", 32, 9, 89, 92, 95, 90, 29, 13, 2.45),
    Pitcher("Frank", "Lewis", "Right", "Right", 32, "6'2\"", 215, "RP", "River Cats", 33, 11, 86, 89, 92, 87, 25, 11, 2.56),
    Pitcher("Patrick", "Walker", "Left", "Left", 27, "6'1\"", 200, "SP", "Iron Wolves", 34, 5, 84, 87, 90, 85, 22, 9, 2.78),
    Pitcher("Jack", "Hall", "Right", "Right", 29, "6'4\"", 225, "RP", "Coastal Kings", 35, 7, 87, 90, 93, 88, 26, 10, 2.34),
]

# ============================================================================
# BATTERS (60 total)
# ============================================================================

BATTERS = [
    # Low skill batters (30-50)
    Batter("Aaron", "Phillips", "Right", "Right", 24, "5'10\"", 180, "C", "River Cats", 11, 2, 38, 35, 42, 8, 45, 120, 0.273),
    Batter("Brandon", "Stewart", "Left", "Left", 26, "5'11\"", 185, "1B", "Iron Wolves", 12, 3, 40, 38, 39, 12, 52, 135, 0.278),
    Batter("Casey", "Murphy", "Right", "Right", 28, "5'9\"", 175, "2B", "Coastal Kings", 13, 4, 36, 40, 44, 15, 58, 142, 0.290),
    Batter("Derek", "Bennett", "Left", "Right", 25, "5'10\"", 182, "3B", "Desert Hawks", 14, 2, 42, 36, 38, 10, 48, 128, 0.272),
    Batter("Eric", "Foster", "Right", "Left", 27, "5'11\"", 188, "SS", "Northside Thunder", 15, 3, 39, 39, 41, 14, 55, 138, 0.285),
    Batter("Frank", "Graham", "Left", "Left", 29, "5'10\"", 180, "LF", "Bay Breakers", 16, 5, 37, 41, 40, 16, 60, 145, 0.293),
    Batter("Gary", "Harris", "Right", "Right", 26, "5'9\"", 178, "CF", "Summit Eagles", 17, 3, 41, 37, 43, 11, 50, 132, 0.275),
    Batter("Henry", "Jackson", "Left", "Right", 28, "5'11\"", 190, "RF", "Lakewood Aces", 18, 4, 38, 40, 39, 13, 54, 140, 0.278),
    Batter("Isaac", "King", "Right", "Left", 25, "5'10\"", 183, "DH", "River Cats", 19, 2, 40, 38, 42, 9, 46, 125, 0.269),
    Batter("Jacob", "Lewis", "Left", "Left", 27, "5'9\"", 176, "C", "Iron Wolves", 20, 3, 36, 42, 40, 17, 62, 148, 0.295),
    Batter("Kevin", "Miller", "Right", "Right", 29, "5'11\"", 192, "1B", "Coastal Kings", 21, 5, 39, 39, 38, 15, 57, 143, 0.285),
    Batter("Lance", "Nelson", "Left", "Right", 26, "5'10\"", 185, "2B", "Desert Hawks", 22, 3, 41, 36, 41, 12, 51, 136, 0.273),
    Batter("Marcus", "Oliver", "Right", "Left", 28, "5'9\"", 179, "3B", "Northside Thunder", 23, 4, 37, 41, 39, 18, 64, 150, 0.299),
    Batter("Nathan", "Parker", "Left", "Left", 25, "5'11\"", 187, "SS", "Bay Breakers", 24, 2, 42, 37, 43, 10, 47, 129, 0.266),
    Batter("Oscar", "Quinn", "Right", "Right", 27, "5'10\"", 181, "LF", "Summit Eagles", 25, 3, 38, 40, 40, 14, 56, 141, 0.284),
    Batter("Peter", "Roberts", "Left", "Right", 29, "5'9\"", 177, "CF", "Lakewood Aces", 26, 5, 40, 38, 42, 16, 61, 146, 0.295),
    Batter("Quentin", "Smith", "Right", "Left", 26, "5'11\"", 189, "RF", "River Cats", 27, 3, 36, 42, 38, 11, 49, 131, 0.272),
    Batter("Raymond", "Taylor", "Left", "Left", 28, "5'10\"", 184, "DH", "Iron Wolves", 28, 4, 41, 39, 41, 13, 53, 137, 0.279),
    Batter("Samuel", "Underwood", "Right", "Right", 25, "5'9\"", 180, "C", "Coastal Kings", 29, 2, 39, 40, 39, 9, 44, 123, 0.264),
    Batter("Thomas", "Vaughn", "Left", "Right", 27, "5'11\"", 191, "1B", "Desert Hawks", 30, 3, 42, 37, 42, 15, 59, 144, 0.291),
    
    # Mid skill batters (51-74)
    Batter("Victor", "Wagner", "Right", "Left", 29, "5'10\"", 185, "2B", "Northside Thunder", 31, 5, 62, 65, 68, 45, 125, 95, 0.568),
    Batter("Walter", "Xavier", "Left", "Left", 26, "5'11\"", 188, "3B", "Bay Breakers", 32, 3, 58, 61, 64, 38, 110, 88, 0.556),
    Batter("Xavier", "Young", "Right", "Right", 28, "5'9\"", 178, "SS", "Summit Eagles", 33, 4, 65, 68, 71, 52, 145, 102, 0.587),
    Batter("Yancy", "Zimmerman", "Left", "Right", 30, "5'10\"", 190, "LF", "Lakewood Aces", 34, 6, 61, 63, 67, 42, 118, 92, 0.562),
    Batter("Zachary", "Adams", "Right", "Left", 27, "5'11\"", 192, "CF", "River Cats", 35, 4, 64, 66, 69, 48, 135, 98, 0.579),
    Batter("Albert", "Baker", "Left", "Left", 29, "5'10\"", 186, "RF", "Iron Wolves", 36, 5, 59, 62, 65, 40, 115, 90, 0.561),
    Batter("Bernard", "Carter", "Right", "Right", 26, "5'9\"", 180, "DH", "Coastal Kings", 37, 3, 63, 64, 68, 46, 128, 96, 0.571),
    Batter("Charles", "Davis", "Left", "Right", 28, "5'11\"", 189, "C", "Desert Hawks", 38, 4, 60, 59, 66, 41, 120, 89, 0.574),
    Batter("Douglas", "Evans", "Right", "Left", 30, "5'10\"", 187, "1B", "Northside Thunder", 39, 6, 66, 67, 70, 50, 142, 100, 0.587),
    Batter("Eugene", "Fisher", "Left", "Left", 27, "5'9\"", 182, "2B", "Bay Breakers", 40, 4, 57, 60, 63, 37, 108, 85, 0.559),
    Batter("Frederick", "Garcia", "Right", "Right", 29, "5'11\"", 191, "3B", "Summit Eagles", 41, 5, 62, 65, 68, 44, 125, 94, 0.571),
    Batter("Gregory", "Harris", "Left", "Right", 26, "5'10\"", 184, "SS", "Lakewood Aces", 42, 3, 58, 61, 64, 39, 112, 87, 0.562),
    Batter("Harold", "Jackson", "Right", "Left", 28, "5'9\"", 179, "LF", "River Cats", 43, 4, 64, 66, 69, 47, 132, 97, 0.576),
    Batter("Irving", "King", "Left", "Left", 30, "5'11\"", 193, "CF", "Iron Wolves", 44, 6, 61, 63, 67, 43, 122, 91, 0.573),
    Batter("Jerome", "Lewis", "Right", "Right", 27, "5'10\"", 186, "RF", "Coastal Kings", 45, 4, 63, 64, 68, 45, 128, 95, 0.574),
    Batter("Kenneth", "Miller", "Left", "Right", 29, "5'9\"", 181, "DH", "Desert Hawks", 46, 5, 59, 62, 65, 40, 116, 89, 0.566),
    Batter("Leonard", "Nelson", "Right", "Left", 26, "5'11\"", 190, "C", "Northside Thunder", 47, 3, 65, 67, 70, 49, 138, 99, 0.582),
    Batter("Maurice", "Oliver", "Left", "Left", 28, "5'10\"", 185, "1B", "Bay Breakers", 48, 4, 60, 59, 66, 41, 119, 88, 0.575),
    Batter("Norman", "Parker", "Right", "Right", 30, "5'9\"", 180, "2B", "Summit Eagles", 49, 6, 62, 65, 68, 46, 130, 96, 0.575),
    Batter("Oliver", "Quinn", "Left", "Right", 27, "5'11\"", 192, "3B", "Lakewood Aces", 50, 4, 58, 61, 64, 38, 110, 86, 0.561),
    
    # High skill batters (75-99)
    Batter("Patrick", "Roberts", "Right", "Left", 29, "5'10\"", 188, "SS", "River Cats", 51, 7, 88, 91, 94, 78, 185, 65, 0.740),
    Batter("Quentin", "Smith", "Left", "Left", 26, "5'9\"", 182, "LF", "Iron Wolves", 52, 4, 85, 88, 91, 72, 168, 58, 0.743),
    Batter("Raymond", "Taylor", "Right", "Right", 28, "5'11\"", 194, "CF", "Coastal Kings", 53, 5, 92, 94, 96, 82, 195, 70, 0.736),
    Batter("Samuel", "Underwood", "Left", "Right", 30, "5'10\"", 189, "RF", "Desert Hawks", 54, 7, 89, 92, 95, 79, 188, 67, 0.738),
    Batter("Thomas", "Vaughn", "Right", "Left", 27, "5'9\"", 183, "DH", "Northside Thunder", 55, 4, 86, 89, 92, 74, 172, 61, 0.738),
    Batter("Ulysses", "Wagner", "Left", "Left", 29, "5'11\"", 191, "C", "Bay Breakers", 56, 6, 90, 93, 95, 80, 192, 68, 0.738),
    Batter("Victor", "Xavier", "Right", "Right", 26, "5'10\"", 186, "1B", "Summit Eagles", 57, 4, 87, 90, 93, 76, 180, 64, 0.738),
    Batter("Walter", "Young", "Left", "Right", 28, "5'9\"", 180, "2B", "Lakewood Aces", 58, 5, 91, 94, 96, 81, 194, 69, 0.738),
    Batter("Xavier", "Zimmerman", "Right", "Left", 30, "5'11\"", 193, "3B", "River Cats", 59, 7, 88, 91, 94, 77, 186, 66, 0.738),
    Batter("Yancy", "Adams", "Left", "Left", 27, "5'10\"", 187, "SS", "Iron Wolves", 60, 4, 89, 92, 95, 78, 189, 67, 0.738),
    Batter("Zachary", "Baker", "Right", "Right", 29, "5'9\"", 181, "LF", "Coastal Kings", 61, 6, 85, 88, 91, 73, 170, 59, 0.742),
    Batter("Albert", "Carter", "Left", "Right", 26, "5'11\"", 192, "CF", "Desert Hawks", 62, 4, 92, 95, 97, 83, 198, 71, 0.735),
    Batter("Bernard", "Davis", "Right", "Left", 28, "5'10\"", 188, "RF", "Northside Thunder", 63, 5, 87, 90, 93, 75, 178, 63, 0.738),
    Batter("Charles", "Evans", "Left", "Left", 30, "5'9\"", 183, "DH", "Bay Breakers", 64, 7, 90, 93, 95, 79, 191, 68, 0.738),
    Batter("Douglas", "Fisher", "Right", "Right", 27, "5'11\"", 194, "C", "Summit Eagles", 65, 4, 86, 89, 92, 74, 174, 62, 0.738),
    Batter("Eugene", "Garcia", "Left", "Right", 29, "5'10\"", 189, "1B", "Lakewood Aces", 66, 6, 91, 94, 96, 80, 193, 69, 0.738),
    Batter("Frederick", "Harris", "Right", "Left", 26, "5'9\"", 182, "2B", "River Cats", 67, 4, 88, 91, 94, 77, 185, 65, 0.740),
    Batter("Gregory", "Jackson", "Left", "Left", 28, "5'11\"", 191, "3B", "Iron Wolves", 68, 5, 89, 92, 95, 78, 188, 67, 0.738),
    Batter("Harold", "King", "Right", "Right", 30, "5'10\"", 187, "SS", "Coastal Kings", 69, 7, 87, 90, 93, 76, 182, 64, 0.739),
    Batter("Irving", "Lewis", "Left", "Right", 27, "5'9\"", 180, "LF", "Desert Hawks", 70, 4, 92, 95, 97, 82, 196, 70, 0.736),
]

# Combine all players
ALL_PLAYERS = PITCHERS + BATTERS

# Verify we have exactly 100 players
assert len(ALL_PLAYERS) == 100, f"Expected 100 players, got {len(ALL_PLAYERS)}"
assert len(PITCHERS) == 40, f"Expected 40 pitchers, got {len(PITCHERS)}"
assert len(BATTERS) == 60, f"Expected 60 batters, got {len(BATTERS)}"

if __name__ == "__main__":
    print(f"Total players: {len(ALL_PLAYERS)}")
    print(f"Pitchers: {len(PITCHERS)}")
    print(f"Batters: {len(BATTERS)}")
    print("\nSample pitcher:")
    print(PITCHERS[0].get_info())
    print(PITCHERS[0].get_stats())
    print("\nSample batter:")
    print(BATTERS[0].get_info())
    print(BATTERS[0].get_stats())
