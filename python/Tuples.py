# A tuple is a collection which is ordered and unchangeable. 
# In Python tuples are written with round brackets.

# Once a tuple is created, you cannot change its values. Tuples are unchangeable.
# It is also possible to use the tuple() constructor to make a tuple.
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))