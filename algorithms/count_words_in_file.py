def count_words(file_path):
    word_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

file_path = 'words.txt'
word_count = count_words(file_path)
print("Number of words in the file:", word_count)


# words.txt
# one two three
# four
# five six seven
# eight nine ten
# eleven twelve thirteen
# fourteen
