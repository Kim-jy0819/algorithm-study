words = list(input())

count_dict = {}
for letter in words:
    letter = letter.upper()
    count_dict[letter] = count_dict.get(letter, 0) + 1

count_sort = sorted(count_dict, key=lambda x : -count_dict[x])

check_multiple_maximum = 0
maximum = 0
maximum_word = ''
for i, key in enumerate(count_sort):
    if i >= 1:
        if maximum == count_dict[key]:
            maximum_word = '?'
        break
    maximum = count_dict[key]
    maximum_word = key
print(maximum_word)