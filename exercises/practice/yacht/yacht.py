# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice_counts = [dice.count(i) for i in range(1, 7)]

    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * dice_counts[category - 1]
    elif category == FULL_HOUSE:
        if sorted(dice_counts).count(2) == 1 and sorted(dice_counts).count(3) == 1:
            return sum(dice)
        else:
            return 0
    elif category == FOUR_OF_A_KIND:
        if 4 in dice_counts:
            return (dice_counts.index(4) + 1) * 4
        elif 5 in dice_counts:
            return (dice_counts.index(5) + 1) * 4
        else:
            return 0
    elif category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
