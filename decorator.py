
def timer(func):
    def inner():
        print('time started')
        # print(func)
        func()
        print('time ended')
    return inner

@timer
def get_factorial():
    print("factorial()")

get_factorial()