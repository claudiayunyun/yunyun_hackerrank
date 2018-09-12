import sys
if __name__ == '__main__':
    #  don't need to use the iterator, eg. for _ in range(10):
    students = []
    min = sys.maxsize
    second_min = sys.maxsize
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        students.append(student)
        if score < min:
            second_min = min
            min = score
        elif score < second_min and score != min:
            second_min = score
    second = []
    for student in students:
        if student[1] == second_min:
            second.append(student[0])
    second.sort()
    for name in second:
        print(name)