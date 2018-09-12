# find the second largest number in the list, which is not equal to the largest
import sys
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = - sys.maxsize
    second_max = - sys.maxsize
    for score in arr:
        if score > max:
            second_max = max
            max = score
        elif score > second_max and score != max:
            second_max = score
    print(second_max)       