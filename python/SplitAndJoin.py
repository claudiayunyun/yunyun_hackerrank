# join() method
# syntax : string.join(iterable)
# iterable	Required. Any iterable object were all the returned values are strings
# A string must be specified as the separator.

def split_and_join(line):
    word_list = line.split(' ')
    result = '-'.join(word_list)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)