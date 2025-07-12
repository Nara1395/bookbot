from stats import get_num_words, get_character_count, generate_report, format_report

def get_book_text(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at f{filepath}...")
    with open(filepath, "r") as f:
        file_contents = f.read()
    return file_contents

def main():

    selected_book = get_book_text("books/frankenstein.txt")
    get_num_words(selected_book)
    char_count_data = get_character_count(selected_book)
    report_data = generate_report(char_count_data)
    format_report(report_data)
    print("============= END ===============")
if __name__ == "__main__":
    main()