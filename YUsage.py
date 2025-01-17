from Yahtzee import YahtzeeRoll

yahtzee = YahtzeeRoll()
print("First roll:", yahtzee.roll_dice())
print("Second roll after rerolling first and third dice:", yahtzee.reroll([0, 2]))
print("Final roll:", yahtzee.get_roll())
#print("Highest current possible score: ", yahtzee.score(yahtzee.get_roll()))
upperHS, lowerHS = yahtzee.score(yahtzee.get_roll())
print("Highest possible upper score:", upperHS)
print("Highest possible lower score:", lowerHS)

