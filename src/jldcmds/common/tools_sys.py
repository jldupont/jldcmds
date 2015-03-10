"""
    Created on 2012-02-12
    @author: jldupont
"""
import logging, types

def dnorm(d):
    """
    Normalize dictionary
    
    >>> dnorm({"SoMeKeY":"  spaces  "})
    {'somekey': 'spaces'}
    """
    r={}
    for e in d:
        try:    r[e.lower()]=d[e].strip()
        except: r[e.lower()]=d[e]
    return r

def info_dump(d, align):
    fmt="%-"+str(align)+"s : %s"

    if type(d)==types.DictionaryType:        
        for key in d:
            logging.info(fmt % (key, d[key]))
            
    if type(d)==types.ListType:
        for el in d:
            key, value=el
            logging.info(fmt % (key, value))

def prepare_callable(module_name, function_name):
    
    ### just import this module if required to
    ### it is not present in python < 2.7
    import importlib
    
    try:
        mod=importlib.import_module(module_name)
    except:
        raise Exception("Can't import module '%s'" % module_name)
        
    try:
        fnc=getattr(mod, function_name)
    except:
        raise Exception("Module '%s' doesn't have a 'run' function" % mod)
    
    if not callable(fnc):
        raise Exception("Can't call 'run' function of callable '%S'" % module_name)
    
    return (mod, fnc)
