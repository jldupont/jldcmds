Various Command Line Tools

@author: Jean-Lou Dupont


* jldcmd-jwrite: write stdin JSON objects to target path


## jldcmd-jwrite

This command waits for line delimited JSON objects, constructs target file names from a pattern and writes the corresponding objects in the target path.  

`jldcmd-jwrite [-d] [-i] -tp targetPath -fp targetFilePattern` 

Where:
- `-d`   : debug mode
- `-i`   : ignore input line objects resulting in write error
- `-tp`  : the target base path to write the objects to
- `-fp`  : the file name pattern
- `-md5` : hash the resulting filename

The `file name pattern` is constructed using a string template with object keys has variables. Optionally, the resulting string can be hashed 
in order to accommodate potentially illegal file names.

Example usage:

`jldcmd-jwrite -i -tp /tmp/objs -fp "$name-$date" -md5`

Would liste to stdin, decode each input line as JSON, use the value of the keys "name" and "date" to construct a filename md5 hashed, 
and finally write the corresponding object to the path `/tmp/objs/hashed_filename`.

History
=======

0.1 : initial release

