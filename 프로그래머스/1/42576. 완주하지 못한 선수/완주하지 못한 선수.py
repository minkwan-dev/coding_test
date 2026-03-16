def solution(participant, completion):
    hash_map = {}
    
    # 1. 모든 참가자를 딕셔너리에 추가하고, 등장 횟수를 기록
    for name in participant:
        if name not in hash_map:
            hash_map[name] = 1
        else:
            hash_map[name] += 1
    
    # 2. 완주자 명단을 순회하며, 해당 이름의 횟수를 차감        
    for name in completion:
        hash_map[name] -= 1
        
    # 3. 횟수가 0이 아닌 선수가, 완주하지 못한 선수    
    for name in hash_map:
        if hash_map[name] > 0:
            return name