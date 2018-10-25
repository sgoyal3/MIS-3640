def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_source = open(source, 'r')
    f_dest = open(dest, 'w')
    
    for line in f_source:
        new_line = line.replace(pattern, replace)
        f_dest.write(new_line)
        
    f_source.close()
    f_dest.close()    


pattern = 'man'
replace = 'woman'
source = 'output.txt'
dest = 'new_' + source
sed(pattern, replace, source, dest)


import os


def walk(dirname):
    """Prints the names of all files in 
    dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)