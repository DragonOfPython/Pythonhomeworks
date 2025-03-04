def create_file(word_count_file):
    print(f"The file '{word_count_file}' does not exist.")
    text = input("Please enter a paragraph to create the file: ")
    with open(word_count_file, 'w') as f:
        f.write(text)
    print(f"File '{word_count_file}' created.")

def read_file(word_count_file):
    with open(word_count_file, 'r') as f:
        return f.read()

def count_words(text):
    # Normalize the text to lowercase and replace punctuation with spaces
    for symbols in ".,!?;:\"'()[]{}":
        text = text.replace(symbols, ' ')
    words = text.lower().split()
    
    # Create a dictionary to count occurrences
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def main_program_run():
    word_count_file = "sample.txt"
    
    # We have to check this file exist or not, if it isn't we have to create
    try:
        with open(word_count_file, 'r'):
            pass
    except FileNotFoundError:
        create_file(word_count_file)

    text = read_file(word_count_file)

    word_counts = count_words(text)
    total_words = sum(word_counts.values())

    # Get user input for top common words
    top_cw = int(input("How many top common words do you want to display? "))
    
    # Sort words by count and get the most common
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    most_common_words = sorted_words[:top_cw]
    #print(most_common_words)

    # Display results
    print(f"\nTotal words: {total_words}")
    print(f"Top {top_cw} most common words:")
    for word, count in most_common_words:
       print(f"{word} - {count} times")

    # Save the output to a new file
    with open("word_count_report.txt", 'w') as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write(f"Top {top_cw} Words:\n")
        for word, count in most_common_words:
            report_file.write(f"{word} - {count}\n")
 

main_program_run()