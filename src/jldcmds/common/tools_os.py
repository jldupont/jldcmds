'''
Created on Mar 9, 2015
@author: jldupont
'''
import os
from types import * #@UnusedWildImport


def safe_mkdir(path, mode=0777):
    """
    Safely creates a directory hierarchy
    
    This function does not throw an exception if the path already exists or
    is created successfully; this behavior contrasts with that of the 
    standard ``os.makedirs`` builtin i.e. throws an error if the path
    already exists.
    
    The function only fails if the child directory and its required parent
    hierarchy can not be created.
    
    The function accepts either a string or a list for the parameter ``path``.
    If ``path`` is a list, the function performs an ``os.path.join`` to construct
    the target path. 
    
    .. Parameters
    
    **Returns**: (existed, path)
    
    The function returns a boolean True if the directory already existed.
     
    """
    # expand list if necessary
    if type(path) is ListType:
        path = os.path.join(*path)

    
    try:    already_exists = os.path.isdir(path)
    except: already_exists = False
    
    if already_exists:
        return True, path
    
    try:    os.makedirs( path, mode )
    except: pass
    
    exists = os.path.exists(path)
    if not exists:
        raise RuntimeError("path[%path] can not be created. Is it a valid directory path?")

    # we obviously had to create it.
    return False, path
