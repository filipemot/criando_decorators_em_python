from functools import wraps

def meu_primeiro_decorator(main_function):
    def inner_function():
        print('decorator')
        return main_function()
    return inner_function

def meu_primeiro_decorator_com_parametros(arg1):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print('decorator')
            print(f"Argument:{arg1}")
            function(*args, **kwargs)
        return wrapper
    return inner_function

@meu_primeiro_decorator
def funcao_com_decorator():
    print('main_function')

@meu_primeiro_decorator_com_parametros('arg1')
def funcao_com_decorator_com_parametros():
    print('main_function')

if __name__ == '__main__':
    funcao_com_decorator()
    funcao_com_decorator_com_parametros()
