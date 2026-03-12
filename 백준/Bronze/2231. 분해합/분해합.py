num = int(input())
min_constructor = 0

# 216 = 198 + 1 + 9 + 8
# 분해합 =  (생성자 X) + (생성자 X의 각 자릿수의 합)
# 완전 탐색의 대상이 생성자 X여야 말이 맞겠슘
# 생성자 X의 각 자릿수 합을 구하는 로직도 필요할 거시다~!
# 그럼 일단 완~~전히 탐색을 해야 하니께 for 문 작성?
# for 문의 범위를 정해야 하는데 생성자는 분해합보다는 당연히 작아야 하지 않을까? ㅇㅈ

for constructor_x in range(num):
    # 분해합을 계산하셈!
    # 각 자릿수의 합은 constructor_x 하나 잡아놓고 for 문 돌리면 될 듯? ㅇㅈ
    ja_rit_su_hap = 0

    for elem in str(constructor_x):
        ja_rit_su_hap += int(elem)

    bun_hae_hap = constructor_x + ja_rit_su_hap

    # 마냑! 분해합이 num이면?
    # min_constructor에 constructor_x를 할당하고 브레이크하면 된다는 거시다~!
    if bun_hae_hap == num:
        min_constructor = constructor_x
        break
    # 다 뒤져봤는데, 조건을 만족하는 constructor_x가 없으면 0을 할당하면 된다는 거시다~!
    else:
        min_constructor = 0

    
print(min_constructor)