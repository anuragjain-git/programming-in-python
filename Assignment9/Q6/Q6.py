def poem(file1):
    file = open(file1, 'r')

    alphabet_count = 0
    space_count = 0
    lowercase_count = 0
    uppercase_count = 0
    vowel_start_count = 0
    beautiful_count = 0

    vowels = "aeiouAEIOU"

    for line in file:
        for char in line:

            if char.isalpha():
                alphabet_count += 1

                if char.islower():
                    lowercase_count += 1
                elif char.isupper():
                    uppercase_count += 1

            elif char.isspace():
                space_count += 1

        words = line.split()
        for word in words:
            if word[0] in vowels:
                vowel_start_count += 1
            if word.lower() == 'beautiful':
                beautiful_count += 1

    file.close()

    print(f"Alphabets : {alphabet_count}")
    print(f"Blank spaces : {space_count}")
    print(f"Lowercase letters : {lowercase_count}")
    print(f"Uppercase letters : {uppercase_count}")
    print(f"Words starting with a vowel: {vowel_start_count}")
    print(f"Occurrences of 'beautiful': {beautiful_count}")


file = 'Poem.txt'
poem(file)
