from stats import get_num_words, num_characters, list, sort_on
import sys

if len(sys.argv) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

    
def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(file_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    character_counts = num_characters(text)
    sorted_chars = list(character_counts)
    sorted_chars.sort(reverse=True, key=sort_on)
    for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
   

main()