# input() function in Python
# Built-in functions, The input() function allows user input.
# input(prompt) prompt	A String, representing a default message before the input.

def print_full_name(a, b):
    print('Hello ' + a + ' ' + b + '! You just delved into python.')


if __name__ == '__main__':
    x = input('Enter your name:')
    print('Hello, ' + x)

    print('Enter your name:')
    y = input()
    print('Hello, ' + y)

    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)