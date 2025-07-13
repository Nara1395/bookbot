from stats import generate_report
import sys

# def get_book_text(filepath):
#     print("============ BOOKBOT ============")
#     print(f"Analyzing book found at f{filepath}...")
#     with open(filepath, "r") as f:
#         file_contents = f.read()
#     return file_contents
#
# def main():
#
#     selected_book = get_book_text("books/frankenstein.txt")
#     get_num_words(selected_book)
#     char_count_data = get_character_count(selected_book)
#     report_data = generate_report(char_count_data)
#     format_report(report_data)
#     print("============= END ===============")

def main():
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        path_to_file = sys.argv[1]
        selected_book = book(path_to_file)
        generate_report(selected_book, path_to_file)

def book(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    main()