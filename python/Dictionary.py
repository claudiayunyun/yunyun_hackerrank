# https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # * : unpack the list or tuple data to other variables dynamically.
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum = 0
    for score in student_marks[query_name]:
        sum += score
    # differences between format() and round()
    print(format(sum/len(student_marks[query_name]), '.2f'))
