# two ways to change an immutable string at specific position
# 1 to convert the string to a list and then change the value.
# 2 to slice the string and join it back.

# change an immutable string use replace()

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)
    # return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)