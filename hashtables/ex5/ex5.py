"""
My solution is not very performant, so running the second test might take a while. 
To remedy this, I suggest that you restrict the input sizes so that it runs faster.
"""

def path_contains_query(path, query):
    split_on_slashes = path.split("/")
    if split_on_slashes[-1] == query:
        return True
    else:
        return False

def finder(files, queries):
    found_files = {}
    result = []
    for f in files:
        if f not in found_files: 
            found_files[f] = False
    
    for q in queries:
        for f in files:
            if path_contains_query(f, q):
                result.append(f)
   
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
