def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    while completion and participant[-1] == completion[-1]:
        participant.pop()
        completion.pop()

    return participant[-1]