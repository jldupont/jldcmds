*NOTICE:*  Work in progress 


Various Command Line Tools

@author: Jean-Lou Dupont


* jldcmd-jwrite: write stdin JSON objects to target path


## jldcmd-jwrite

This command waits for line delimited JSON objects, constructs target file names from a pattern and writes the corresponding objects in the target path.  

`jldcmd-jwrite` [-d] [-i] -tp targetPath -fp targetFilePattern 

Where:
- `-d`  : debug mode
- `-i`  : ignore input line objects 
- `-tp` : the target base path to write the objects to
- `-fp` : the file name pattern

The `file name pattern` is constructed using  


History
=======

0.1 : initial release

