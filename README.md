## UTILS

collects the most frequently used code snippets by moi, 
put these here so that i don't have to write everything
again

don't get into the design details/trade offs very soon,
as long as it speeds up development cycle (probably
should just learn fast.ai and its 'fast' dependencies?)

frequently used packages: see requirements.txt

should develop this using 'nbdev' (and update the pkg 
inside a docker container, the way we used to do)

### Note:

develop this repo with nbdev (or at least .ipynb)

### Debugging

decorator
ref [link](https://myapollo.com.tw/blog/python-decorator-tutorial/?fbclid=IwAR117iqq2OBvH3AiROpI_zThUBrm54_5NJm-5Nb547gS_JsBUdwBwM7TU0g)

// basic
```python
def debug(func):
    print("func:", func.__name__)
    def wrapper(*args, **kwargs):
        print("plugin args", args)
        print("plugin kwargs", kwargs)
        func(*args, **kwargs)
    return wrapper
```

// advanced ones
// to fix 'doc-string vanishing problem'
// use custom-defined 'timeit' function as an example
```python
from time import time, sleep
from functools import wraps
def timeit(func):
    @wraps
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print("total time spent on %s: %.3f" % (func.__name__, end - start))
    return wrapper

## usage
@timeit
def sleep_10s():
    """sleep for 10 sec"""
    sleep(10)
    return

### doc-string will now be printed
print("func name: %s\ndoc-string: %s" % (func.__name__, func.__doc__))
```

