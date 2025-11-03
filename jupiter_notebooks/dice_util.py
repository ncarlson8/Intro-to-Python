import random


def roll_die():
    '''Rolls one die at random and returns a number inclusive of 1 through 6'''
    return random.randint(1, 6)

def roll_two_die():
    '''Rolls two dice and returns a number inclusive of 2 and 12'''

    die_one = roll_die()
    die_two = roll_die()

    return die_one + die_two

def roll_n_sided_die(sides):
    '''Returns a number between 1 and `sides`''' 
    return random.randint(1, sides)
    
def roll_n_sided_dice(sides, dice):
    '''Returns a number that is computed by adding up the
       value of multiple dice of n-sides'''
    
    # Let's declare a variable to hold all our rolls
    final_roll = 0

    # We will call `roll_n_sided_die` multiple times
    # To be precise, we will roll it the number of times
    # specified in the variable `dice`. We'll use a loop
    for roll in range(dice):
        roll = roll_n_sided_die(sides)
        final_roll = final_roll + roll
    
    return final_roll
