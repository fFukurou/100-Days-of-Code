import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("hello")
    
@delay_decorator
def say_bye():
    print("bye")

@delay_decorator
def say_die():
    print("die")

@delay_decorator    
def say_omoshiroi():
    print("omoshiroi")


say_omoshiroi()


decorated_function = delay_decorator(say_die)
decorated_function()