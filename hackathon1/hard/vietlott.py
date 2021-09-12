from itertools import permutations, combinations

possible_bet_type = [x for x in range(5,19) if x != 6 and x != 17]

def power_6_45_ticket(bet_type, user_panel):
    assert(bet_type in possible_bet_type)
    assert(bet_type == len(user_panel))
    assert(0 < all(user_panel) <= 45)
    ans = []
    if bet_type != 5:
        ans = list(combinations(user_panel, 6))
    else:
        for x in range(1,46):
            if x not in user_panel:
                new_panel = user_panel.copy()
                new_panel.append(x)
                ans.append(tuple(new_panel))
    return ans