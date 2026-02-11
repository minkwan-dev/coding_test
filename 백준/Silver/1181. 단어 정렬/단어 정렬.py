T = int(input())

words_list = []

for tc in range(1, T + 1):
    word = input()
    words_list.append(word)


set_words_list = set(words_list)
re_words_list = list(set_words_list)

re_words_list.sort(key=lambda x: (len(x), x))
            
for word in re_words_list:
    print(word)