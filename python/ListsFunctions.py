if __name__ == '__main__':
    N = int(input())
    the_list = []
    for _ in range(N):
        function, *arg = input().split()
        arg = list(map(int, arg))
        if function == 'insert':
            the_list.insert(arg[0],arg[1])
        elif function == 'print':
            print(the_list)
        elif function == 'remove':
            the_list.remove(arg[0])
        elif function == 'append':
            the_list.append(arg[0])
        elif function == 'sort':
            the_list.sort()
        elif function == 'pop':
            the_list.pop()
        elif function == 'reverse':
            the_list.reverse()