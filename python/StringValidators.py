if __name__ == '__main__':
    s = input()
    has_alphanumeric = False
    has_alphabetical = False
    has_digit = False
    is_lower = False
    is_upper = False
    for char in list(s):
        if char.isalnum():
            has_alphanumeric = True
        if char.isalpha():
            has_alphabetical = True
        if char.isdigit():
            has_digit = True
        if char.islower():
            is_lower = True
        if char.isupper():
            is_upper = True
    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digit)
    print(is_lower)
    print(is_upper)