def get_num_words(content):
    words = content.split()
    num_words = len(words)
    # print("----------- Word Count ----------")
    # print(f"Found {num_words} total words")
    return num_words

def get_char_count(content):
    character_count = {}
    for character in content.lower():
        if character in character_count.keys():
            character_count[character] = character_count[character] + 1
        else:
            character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def format_char_count_only_alphabets(all_characters_dict):
    list_of_alpha_count = []
    for letter, count in all_characters_dict.items():
        if letter.isalpha():
            list_of_alpha_count.append({"char": letter, "num": count})
    list_of_alpha_count.sort(reverse=True, key=sort_on)
    return list_of_alpha_count

def generate_report(content, path_to_file):
    word_count = get_num_words(content)
    all_character_count = get_char_count(content)
    alpha_count_only = format_char_count_only_alphabets(all_character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for individual_char_count in alpha_count_only:
        print(f"{individual_char_count['char']}: {individual_char_count['num']}")
    print("============= END ===============")
