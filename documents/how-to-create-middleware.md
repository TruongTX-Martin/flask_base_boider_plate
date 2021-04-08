## What is middleware?

**Middleware** is computer software that provides services to software applications beyond those available from the operating system. It can be described as "software glue".
([Wiki reference](https://en.wikipedia.org/wiki/Middleware))


## How to middleware work?

    For example if you want to log every request middleware may useful in that case.
    Client → Server → Middleware → Server side Application


## What is middleware implement?

* [Decorator pattern](https://en.m.wikipedia.org/wiki/Decorator_pattern)
    * [Decorator in Flask](https://flask.palletsprojects.com/en/master/patterns/viewdecorators/)
* [WSGI](https://en.m.wikipedia.org/wiki/Web_Server_Gateway_Interface)
    * [The Explicit Application Objec](https://flask.palletsprojects.com/en/1.1.x/design/?highlight=middleware#the-explicit-application-object)

## How to create middleware?

Use `Decorator pattern`

#### 1. A simple example about middleware by wrap

In middleware file
```
from functools import wraps
from flask import g, request, redirect, url_for

def greeting(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('Hello, this message is showed in your log.')
        return f(*args, **kwargs)
    return decorated_function
```

In route file
```
@app.route('/secret_page')
@greeting
def secret_page():
    pass
```

#### 2. Add params in wrap 

In middleware file
```
from functools import wraps
from flask import request

def greeting_with_params(name = 'Anonymous', age = 33):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            print('Hello {}, you are {}. This message is showed in your log.'.format(name, age))
            return f(*args, **kwargs)
        return decorated_function
    return decorator
```

[Reference](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/)