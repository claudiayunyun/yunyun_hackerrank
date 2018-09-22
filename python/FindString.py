# string find()
# The find() method finds the first occurrence of the specified value.
# The find() method returns -1 if the value is not found.
# syntax : string.find(value, start, end)

# string rfind()
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
# syntax : string.rfind(value, start, end)

# value	Required. The value to search for
# start	Optional. Where to start the search. Default is 0
# end	Optional. Where to end the search. Default is to the end of the string

def count_substring(string, sub_string):
    index = 0
    count = 0
    while string.find(sub_string, index) != -1:
        index = string.find(sub_string, index) + 1
        count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)