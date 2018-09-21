# lambda expression
##syntax : lambda arguments : expression

# map function
# map(function, iterables)
# function	Required. The function to execute for each item
# iterable	Required. A sequence, collection or an iterator object. 
#           You can send as many iterables as you like, 
#           just make sure the function has one parameter for each iterable.

def swap_case(s):
    result = map(lambda char: char.upper() if char.islower() else char.lower(), list(s))
    return ''.join(list(result))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


