# For extra reading on this: https://pythongeeks.org/python-variable-scope/

# foo = 'hello'

# def func():
#     print(foo)

# print(foo)


###################################


# def func():
#     foo = 'hello'

# print(foo)


###################################


# foo = 'hello'

# def func():
#     foo = 'world'
#     print(foo)

# print(foo)
# func()
# print(foo)


###################################


# foo = 3

# def func():
#     # global foo
#     print(foo)
#     foo = foo + 3
#     print(foo)

# func()
# print(foo)


###################################


# def outer():
#     x="Python"
#     print("Value of x in outer function:",x)
#     def inner():
#         global x
#         x="PythonGeeks"
#         print("Value of x in inner function:",x)
#     inner()
#     print("Value of x in outer function after calling inner function:",x)

# outer()
# print("Value of x outside the functions:",x)