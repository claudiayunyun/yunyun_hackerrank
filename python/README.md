## Python Code Practice of HackerRank  
### differences between format() and round()  
```python
# Dictionary.py
print(round(2,2)) # 2
print(round(2.348,2)) # 2.34
print(format(2,'.2f')) # 2.00
``` 
### single asterisk and double asterisk in Python  
```python
# Dictionary.py
numbers = [1,2,3,4,5,6]
a, *b = numbers # a = 1, b = [2,3,4,5,6]
```

### use single asterisk notation list as arguments of function
```python
the_list = [5,7]
*line,  = input().split()
args = list(map(int, line))
the_list.insert(*args)
print(the_list)
*line,  = input().split()
args = list(map(int, line))
the_list.remove(*args)
print(the_list)
```