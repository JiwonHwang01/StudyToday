def solution(players, callings):
    result = {player:i for i, player in enumerate(players)}
    
    for call in callings:
        idx = result[call]
        result[call] -= 1
        result[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))