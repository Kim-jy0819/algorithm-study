student_num = int(input())

student_infos = [[]]
for _ in range(student_num):
    student_infos.append(list(map(int, input().split())))

class_dict = {
    1: dict(),
    2: dict(),
    3: dict(),
    4: dict(),
    5: dict(),
}
for student in range(1, student_num+1):
    for grade in range(1,6):
        class_num = student_infos[student][grade-1]
        class_dict[grade][class_num] = class_dict[grade].get(class_num, set([])) | set([student])

maximum = 0
captain = 0
for student in range(1, student_num+1):
    friend_list = set([])
    for grade in range(1,6):
        class_num = student_infos[student][grade-1]
        friend_list |= class_dict[grade][class_num]
    if maximum < len(friend_list):
        maximum = len(friend_list)
        captain = student

print(captain)
