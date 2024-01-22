def count_words_and_vowels(file1):

    file = open(file1, 'r')
    content = file.read()

    wordCount = len(content.split())

    vowels = "aeiouAEIOU"
    vowelCount = 0

    for char in content:
        if char in vowels:
            vowelCount += 1
    
    file.close()
    print(f"Words : {wordCount}")
    print(f"Vowels : {vowelCount}")

file1="file1.txt"
count_words_and_vowels(file1)
