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

### Note
As a workaround to 'fold' feature in html, use the <details> and <summary> tags. It even works on Github:
<details>
<summary>click here</summary>
made you look.

(code example here, but let's not get recursive!)
</details>

#### TODO

### Debugging

#### Python

built-in methods, etc

ipython debugger (of course): one can always use this to lookup definitions quickly

globals(): Return the dictionary containing the current scope's global variables.

    NOTE: Updates to this dictionary *will* affect name lookups in the current
    global scope and vice-versa.

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

use wrapper function to decorate 'print()'

one should just use pysnooper

```python
"use callback function to avoid typing 'print_it' the whole time"

print_it=True # prints it like print, else, don't print a thing

def print_fn(func):
  def wrap(*args,**kwargs):
    if print_it:
      func(*args, **kwargs)
  return wrap

@print_fn
def print_(*args, **kwargs):
  return print(*args, **kwargs)
```

### fetch

when downloading code snippets from github (e.g., just 1 instead of the whole repo), use snippets below to not press 'Raw' button
```python
def _parse_github(url):
    # url: url of the page / file, expecting starting with 'https://github.com/...'
    return url.replace("github.com","raw.githubusercontent.com").replace("/blob", "")
```

### deep learning

we should do a seperate file so that time expense on importing won't be too long?

```python
# clear some memory in gpu using torch
torch.cuda.empty_cache()

```

### TODO

fastai stuff: fastcore, etc; e.g., @patch (in fastcore/basic.py) can be very versatile

