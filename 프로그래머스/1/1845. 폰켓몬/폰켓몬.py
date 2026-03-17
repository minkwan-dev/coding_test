def solution(nums):
    # 1. 해시 테이블을 생성
    hash_map = {}
    
    # 2. 각 폰켓몬 번호를 Key로 하여 카운팅
    for n in nums:
        if n in hash_map:
            hash_map[n] += 1
        else:
            hash_map[n] = 1
            
    # 3. hash_map의 Key의 개수가 곧 폰켓몬의 종류 수
    unique_count = len(hash_map)
    
    # 4. 내가 가져갈 수 있는 최대치(N/2)를 계산
    limit = len(nums) // 2
    
    # 5. 종류 수와 최대치 중 작은 값을 반환
    return min(unique_count, limit)