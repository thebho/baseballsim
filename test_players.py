from players import get_all_pitchers, get_all_batters

pitchers = get_all_pitchers()
batters = get_all_batters()

print('Sample pitchers:')
for p in pitchers[:5]:
    print('  ' + p.name + ' - Rating: ' + str(p.getRating()) + ', Throws: ' + p.throwingHand)

print('\nSample batters:')
for b in batters[:5]:
    print('  ' + b.name + ' - Contact: ' + str(b.getRating()) + ', Bats: ' + b.battingHand)

print('\nAll pitcher ratings:')
for p in pitchers:
    assert 1 <= p.getRating() <= 99, 'Rating out of range for ' + p.name
print('  All pitcher ratings valid (1-99)')

print('\nAll batter contacts:')
for b in batters:
    assert 1 <= b.getRating() <= 99, 'Contact out of range for ' + b.name
print('  All batter contacts valid (1-99)')
