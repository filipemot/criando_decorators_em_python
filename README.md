**Criando Decorators em Python em funções**

Decorators são funções que modificam o comportamento de outras funções. Várias vezes temos a necessidade de antes de executar uma função específica, modificar ou validar alguma informação para depois executa-la.

Vários frameworks da linguagem já utiliza desse recurso para modificar a execução de algumas funções.

Por exemplo em flask, temos o decorator @app.route, que é utilizado para definir as rotas de uma api. 

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()
```

Vejamos que nesse exemplo a função hello_world, tem apenas uma sintaxe que retorna uma string 

"Hello World", porém a parte de tratar o método e executá-lo como uma api é feito pelo decorator app.route. Sendo assim toda essa parte foi abstraído pelo decorator.

**Criando o primeiro decorator**

Decorator em python nada mais é que uma função, para criá-lo basta criar uma função.

```python
def meu_primeiro_decorator(main_function):
    def inner_function():
        print('decorator')
        return main_function()
    return inner_function
```

Agora para utilizar esse decorator basta coloca-lo em cima de uma outra função:

```python
@meu_primeiro_decorator
def funcao_com_decorator():
    print('main_function')
```

Quando executamos o nosso código obtemos o valor:

```python
decorator
main_function
```

Vejamos que pela ordem de execução do nosso decorator, primeiramente é executado o print('decorator') e logo após é executado a outra função.

**Criando o primeiro decorator com parâmetro**

Podemos também criar decorators com parâmetros

```python
def meu_primeiro_decorator_com_parametros(arg1):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print('decorator')
            print(f"Argument:{arg1}")
            function(*args, **kwargs)
        return wrapper
    return inner_function
```

Agora para utilizar esse decorator basta coloca-lo em cima de uma outra função e atribuir o valor do parâmetro

```python
@meu_primeiro_decorator_com_parametros('arg1')
def funcao_com_decorator_com_parametros():
    print('main_function')
```

Quando executamos o nosso código obtemos o valor:

```python
decorator
Argument:arg1
main_function
```

Vejamos que pela ordem de execução do nosso decorator, primeiramente é executado o print('decorator'), depois  print(f"Argument:{arg1}") e logo após é executado a outra função.

**GitHub**

[https://github.com/filipemot/criando_decorators_em_python](https://github.com/filipemot/criando_decorators_em_python)