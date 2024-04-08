import copy

def cal_prob(letter_count_dict):
    L, O, V, E = letter_count_dict.values()
    return ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

green_name = input()
count_dict = {
    'L':0,
    'O':0,
    'V':0,
    'E':0
}
for letter in green_name:
    if letter in count_dict:
        count_dict[letter] += 1.0

count_list = []
candidate_num = int(input())
candidates = []
result_list = []
for i in range(candidate_num):
    team_name=input()
    letter_count_dict = copy.deepcopy(count_dict)
    for letter in team_name:
        if letter in letter_count_dict:
            letter_count_dict[letter] += 1.0

    # 확률 계산
    prob = cal_prob(letter_count_dict)
    result_list.append([prob, team_name])
result_list = sorted(result_list, key= lambda x: (-x[0], x[1]))
print(result_list[0][1])