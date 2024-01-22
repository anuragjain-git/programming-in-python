def store_data_in_file(file1):

    file = open(file1, 'w')

    while True:

        user_input = input("Enter : ")

        if not user_input:
            break

        capitalize_input = user_input.capitalize()
        file.write(capitalize_input + '\n')

    file.close()
    print("Data has been stored")

file = "file1.txt"
store_data_in_file(file)
