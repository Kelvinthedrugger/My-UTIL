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

