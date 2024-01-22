def add_newline_and_write(file1, file2):

    f1 = open(file1, 'r')
    f2 = open(file2, 'w')

    for line in f1:
        newline = line.rstrip('\n') + '\n'
        f2.write(newline)
    
    f1.close()
    f2.close()
    print(f"Contents of {file1} is written to {file2}")
    
file1='file1.txt'
file2='file2.txt'
add_newline_and_write(file1, file2)
