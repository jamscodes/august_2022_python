my_age = 26

def outer():
    x="Python"
    print(x)
    def inner():
        # global x
        x="PythonGeeks"
        print(x)
    inner()
    print(x)
    print(my_age)

outer()
print(x)

# Python,