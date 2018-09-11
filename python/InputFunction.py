# input() function in Python
# Built-in functions, The input() function allows user input.
# input(prompt) prompt	A String, representing a default message before the input.

if __name__ == '__main__':
    x = input('Enter your name:')
    print('Hello, ' + x)

    print('Enter your name:')
    y = input()
    print('Hello, ' + y)