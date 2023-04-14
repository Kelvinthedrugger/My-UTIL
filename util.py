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

