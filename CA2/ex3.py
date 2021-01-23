from random import choice, randint


def five_a_side_selector(names: list) -> list:
    """This function takes in a list of names then split up the list of names into teams as follows. If there are less than 20 
    names in the list the function should make sure that no teams have any subs and the teams should be equal as possible. If there 
    are more than 20 names the function should create as many full teams as possible and allow for one sub per team. The function 
    should then return a list with nested lists containing the names of players."""

    teams_list = []

    if type(names) != list:
        print('Please parse a list of names to this function')
        return None
    for name in names:
        if type(name) != str:
            print('Please parse a list of names containing all strings')
            return None

    if len(names) < 20:
        divisors = [x for x in range(1, len(names)+1)]
        possible_divisors = []
        target = 5
        dtarget = 0
        for divisor in divisors:
            if len(names) % divisor == 0:
                possible_divisors.append(divisor)
        if len(names) in possible_divisors and 1 in possible_divisors and len(possible_divisors) == 2:
            chosen_divisor = 5
        else:
            chosen_divisor = min(
                possible_divisors, key=lambda x: abs(x-target))
       # The following piece of code above creates a divisor which looks for
       # a divisor which will produce the most equally distributed teams
        quotient = len(names)//chosen_divisor
        for x in range(quotient):
            new_team = []
            for players in range(chosen_divisor):
                new_player = choice(names)
                new_team.append(new_player)
                names.remove(new_player)
            teams_list.append(new_team)
            # Here the optimal amount of players determined by chosen divisor are chosen
            # and removed from the list accordingly

        if len(names) >= 1:
            for x in range(len(names)):
                sub_player = choice(names)
                teams_list[randint(0, len(teams_list)-1)].append(sub_player)

    elif len(names) > 20:
        quotient = len(names)//5
        for x in range(quotient):
            new_team = []
            for players in range(5):
                new_player = choice(names)
                new_team.append(new_player)
                names.remove(new_player)
            teams_list.append(new_team)
        if len(names) >= 1:
            for y in range(len(teams_list)):
                sub_player = choice(names)
                teams_list[randint(0, len(teams_list)-1)].append(sub_player)
        # Here the code splits the team into as many teams of 5 as possible
        # Then if there are any remainders it picks a random player to add as a substitute
    return teams_list
