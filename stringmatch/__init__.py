from _stringmatch import ffi, lib

def match(a, b):
    return lib.match(a.encode('utf8'), b.encode('utf8'))
