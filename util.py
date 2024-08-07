## we put 'import xx' in the function
## to avoid kickstarting for too long

# fetching a part of it, writing a part of it
# ref: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url, fname=""):
    import requests
    if len(fname) == 0:
        # TODO: consider to check for existing files here?
        fname = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment 'if'
                # and set chunk_size parameter to None.
                if chunk:
                    f.write(chunk)
    return fname

def _parse_github(url):
    # url: url of the page / file, expecting starting with 'https://github.com/...'
    return url.replace("github.com","raw.githubusercontent.com").replace("/blob", "")


# fast ai, deep learning related ones
## convert cells with '#' in .ipynb to .py
## one can use 'nbdev' lib in fast.ai (github
## faculty, not the fastai lib per se), but
## requires complete config
def is_export(cell):
    import re
    if cell['cell_type'] != 'code': return False
    src = cell['source']
    if len(src) == 0 or len(src[0]) < 7: return False
    # |export, if you want to use just 'export', remove the '|' below
    return re.match(r'^\s*#\s*|export\s*$', src[0], re.IGNORECASE) is not None

def notebook2script(fname):
    import re
    import json
    from pathlib import Path
    fname = Path(fname)
    fname_out = f'nb_{fname.stem}.py'
    main_dic = json.load(open(fname, 'r'))
    code_cells = [c for c in main_dic['cells'] if is_export(c)]
    module = f'''
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/{fname.name}

'''
    for cell in code_cells: module += ''.join(cell['source'][1:]) + '\n\n'
    module = re.sub(r' +$', '', module, flags=re.MULTILINE)
    open(fname.parent/fname_out, 'w').write(module[:-2])
    print(f"Converted {fname} to {fname_out}")

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
    tasks: list of arguments to 'func', covered with a tuple
           e.g., (arg_1, arg_2)
    """
    # TODO: parse **kwargs so that it fits the format?
    #def wrap_it(*args, **kwargs):
    def wrap_it(tasks):
        import multiprocessing
        processes = []
        for task in tasks:
            # not tested
            if not isinstance(task, tuple):
                task = (task,)
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

## to see how much space per variable occupies in memory
def sizeof_fmt(num, suffix='B'):
    ''' by Fred Cirera,  https://stackoverflow.com/a/1094933/1870254, modified'''
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)

def get_variable_size(size=10):
    from sys import getsizeof
    """# can be 'locals()' or 'globals()'"""
    for name, size in sorted(((name, getsizeof(value)) for name, value in list(
                              globals().items())), key= lambda x: -x[1])[:size]:
        print("{:>30}: {:>8}".format(name, sizeof_fmt(size)))

