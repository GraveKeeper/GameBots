import Units as units

unit = units.Unit('acc', 'crit', 100, 50, 10, 60, 100, 100)
unit.accuracy = 'cca'
print(unit.accuracy)