'''
    Created on Mar 10, 2015
    @author: jldupont
'''
from string import Template
import hashlib

def construct_filename(input_json_object, filename_pattern, hash_md5 = False):
    """
    >>> j = { "key1": "value1", "key2": "1234" }
    >>> construct_filename(j, "$key1 ==> $key2")
    'value1 ==> 1234'
    
    >>> construct_filename(j, "$key1 ==> $key2, $unknown_var")
    'value1 ==> 1234, $unknown_var'
    
    """
    filename_tpl = Template( filename_pattern )
    
    filename = filename_tpl.safe_substitute( input_json_object )
    
    if hash_md5:
        
        m = hashlib.md5()
        m.update(filename)
        
        return m.hexdigest()
    
    return filename

    
if __name__=="__main__":
    import doctest
    doctest.testmod()
    