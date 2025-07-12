def get_num_words(text):
    print("----------- Word Count ----------")
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_character_count(text):
    print("--------- Character Count -------")
    char_count_ledger = {}
    for character in text.lower():
        if character in char_count_ledger.keys():
            char_count_ledger[character] = char_count_ledger[character] + 1
        else:
            char_count_ledger[character] = 1
    return char_count_ledger

def sort_on(items):
    return items["num"]

def generate_report(dict_char_counts):
    report_data = []
    for key, value in dict_char_counts.items():
        if key.isalpha():
            data_entry = {"char": key, "num": value}
            report_data.append(data_entry)
        else:
            # print(f"This is not a char: {key}")
            continue
    return report_data

def format_report(report_data):
    for char_data in report_data:
        character_to_print = ""
        character_number = 0
        for key, value in char_data.items():
            if key == "char":
                character_to_print = value
            if key == "num":
                character_number = value
        print(f"{character_to_print}: {character_number}")




    report_data.sort(reverse=True, key=sort_on)
    return report_data
