the_list = [5,7]
*line,  = input().split()
args = list(map(int, line))
the_list.insert(*args)
print(the_list)
*line,  = input().split()
args = list(map(int, line))
the_list.remove(*args)
print(the_list)

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

# dispatch?
# switch case in python
# function in dict
# use map function