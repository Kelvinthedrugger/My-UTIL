# fetching a part of it, writing a part of it
# ref: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url, fname=""):
    #fname = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                if chunk:
                    f.write(chunk)
    return fname


# Callbacks

## decorator for multi-processing
## ref to my impl: https://github.com/Kelvinthedrugger/-AI-/blob/main/PLURK/PLURK_EZ_GET/ultimate_fetch.py#L132
"not tested! not sure if @mult is better than just mult(func, tasks)"
def mult(func, tasks):
    """
    run 'func' with multi-processing
    usage:
        @mult
        def fun1():
            ...
    """
    # TODO: parse **kwargs so that it fits the format?
    #def wrap_it(*args, **kwargs):
    def wrap_it(tasks):
        import multiprocessing
        processes = []
        for task in tasks:
            task = tuple(task) # not tested
            p = multiprocessing.Process(target=func, args=task)
            processes.append(p)
            p.start()

        for process in processes:
            process.join()
    return wrap_it


## timing function
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

## print_(), a slightly more convenient print()
print_it=True # prints it like print, else, don't print a thing
def print_fn(func):
    "decorator for print_(), can be used to anything that needs to be controlled by print_it (defaults to True)"
    def wrap(*args,**kwargs):
        if print_it:
            func(*args, **kwargs)
    return wrap

@print_fn
def print_(*args, **kwargs):
    "use callback function to avoid typing 'print_it' the whole time"
    return print(*args, **kwargs)

