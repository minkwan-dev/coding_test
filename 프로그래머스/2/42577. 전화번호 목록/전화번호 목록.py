def solution(phone_book):
    result = True
    hash_map = {}
    
    # 1. 전화번호 해시맵 등록
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 2. 전화번호 목록 순회
    for phone_number in phone_book:
        curr = ''        
        # 3. 전화번호 요소 순회
        for number in phone_number:
            curr += number
            # 4. curr가 해시맵에 있으며, 전화번호 자체가 아니라면 result = False
            if curr in hash_map and curr != phone_number:
                result = False
    
    return result