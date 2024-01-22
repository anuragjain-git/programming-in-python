def copy_alternative_lines(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'w') as f2:
            lines = f1.readlines()

            for i, line in enumerate(lines):
                # check according to indexing: 0,1,2,...
                if i % 2 == 0:
                    f2.write(line)
        print("Copied")

    except FileNotFoundError:
        print("File not found error")

    except Exception as e:
        print(f"exception occured: {e}")
file1 = 'file1.txt'
file2 = 'file2.txt'
copy_alternative_lines(file1, file2)
