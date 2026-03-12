def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # unpacks list into positional args

info = {"a": 10, "b": 20, "c": 40}
print(add(**info))  # unpacks dict into keyword args