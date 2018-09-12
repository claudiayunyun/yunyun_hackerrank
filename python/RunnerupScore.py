# find the second largest number in the list, which is not equal to the largest
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = 0
    second_max = 0
    for score in arr:
        if score > max:
            second_max = max
            max = score
        elif score > second_max and score != max:
            second_max = score
    print(second_max)       