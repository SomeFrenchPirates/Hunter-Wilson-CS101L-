#Introdcution
print('Welcome to the Text Processing Program')

def receive_original_text():
    original_text = input('Put down your original text here:')
    words = []
    words.append(original_text)
    return original_text

receive_original_text()
print('Text Analysis Options\n', '1. Word Count\n', '2. Longest Word\n','3. Count of Substring\n', '4. Unique Words\n', '5. Exit')
Option = int(input('Choose an Operation 1-5:'))


def word_count(text):
    receive_original_text()
    words = []
    words.append(original_text)
    text = len(words)
    return words

def find_longest_word(text):
    pass

def count_substring(text, substring):
    receive_original_text()
    text = original_text
    substring = original_text
    return substring#[,,]

def extract_unique_words(text):
    pass

def main():
    print('Text Analysis Options\n', '1. Word Count\n', '2. Longest Word\n','3. Count of Substring\n', '4. Unique Words\n', '5. Exit')
    Option = int(input('Select an Analysis Option 1-5:'))
    while Option <= 5:
        if Option == 1:
            word_count(text)
            main()
            continue
        if Option == 2:
            find_longest_word(text)
            main()
            continue
        if Option == 3:
            count_substring(text, substring)
            main()
            continue
        if Option == 4:
            extract_unique_words()
            main()
            continue
        if Option == 5:
            print('Goodbye!')
            break
        if Option > 5:
            main()
            continue

if __name__ == "__main__":
    main()





























