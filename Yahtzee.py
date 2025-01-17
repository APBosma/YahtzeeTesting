import random

class YahtzeeRoll:
    def __init__(self, num_dice=5, sides=6):
        self.num_dice = num_dice
        self.sides = sides
        self.roll = []

    def roll_dice(self):
        self.roll = []  # Reset the roll
        for _ in range(self.num_dice):
            die_value = random.randint(1, self.sides)
            self.roll.append(die_value)
        return self.roll

    def reroll(self, indices):
        for index in indices:
            if 0 <= index < self.num_dice:
                self.roll[index] = random.randint(1, self.sides)
        return self.roll

    def get_roll(self):
        return self.roll

# Literally just found out python has switch statements and that is CRAZY
# I only checked just in case cause these seemed like a good time to use one
    def score(self, roll):
        yahtzee = 0
        aKind = 0
        house = 0
        straight = 0
        valueOnes = 0
        valueTwos = 0
        valueThrees = 0
        valueFours = 0
        valueFives = 0
        valueSixes = 0
        for num in roll:
            match num:
                case 1:
                    valueOnes += 1
                case 2:
                    valueTwos += 1
                case 3:
                    valueThrees += 1
                case 4:
                    valueFours += 1
                case 5:
                    valueFives += 1
                case 6:
                    valueSixes += 1
                case _:
                    print("There is a number that shouldn't be on the dice")
                    
        #chance = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        
        # 3 of a kind or 4 of a kind testing
        if (valueSixes == 3 or valueSixes == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        elif (valueFives == 3 or valueFives == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        elif (valueFours == 3 or valueFours == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        elif (valueThrees == 3 or valueThrees == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        elif (valueTwos == 3 or valueTwos == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        elif (valueOnes == 3 or valueOnes == 4):
            aKind = valueOnes + (valueTwos * 2) + (valueThrees * 3) + (valueFours * 4) + (valueFives * 5) + (valueSixes * 6)
        
        #small + large straight check
        if (valueOnes !=0 and valueTwos != 0 and valueThrees != 0 and valueFours != 0):
            if (valueFives !=0):
                straight = 40
            else:
                straight = 30
        elif (valueTwos != 0 and valueThrees != 0 and valueFours != 0 and valueFives != 0):
            if (valueOnes != 0 or valueSixes != 0):
                straight = 40
            else:
                straight = 30
        elif (valueThrees != 0 and valueFours != 0 and valueFives != 0 and valueSixes != 0):
            straight = 30
            
        #house
        if ((valueOnes == 3 or valueTwos == 3 or valueThrees == 3 or valueFours == 3 or valueFives == 3 or valueSixes == 3) and
            (valueOnes == 2 or valueTwos == 2 or valueThrees == 2 or valueFours == 2 or valueFives == 2 or valueSixes == 2)):
            house = 25
        
        #Yahtzee
        if (valueOnes == 5 or valueTwos == 5 or valueThrees == 5 or valueFours == 5 or valueFives == 5 or valueSixes == 5):
            yahtzee = 50
            
        highScore = max(aKind, house, straight, yahtzee)
        upperHighScore = max(valueOnes, valueTwos*2, valueThrees*3, valueFours*4, valueFives*5, valueSixes*6)
            
        #print("Highest possible upper score:", upperHighScore)
        #print("Highest possible lower score:", highScore)
        return upperHighScore, highScore
    
    
    
    
    
    
    
    
