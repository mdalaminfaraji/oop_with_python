def double_decker():
    print('something ')
    def inner_fun():
        print('inner fn')
        return 30
    return inner_fun
print(double_decker()())

def do_something(work):
    print('work start')
    work()
    print("work end")

def fun():
    print('work middle')
do_something(fun)