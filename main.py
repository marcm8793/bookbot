def main():
    with open("books/frankenstein.txt", "r") as file:
        text = file.read()

    def count_words(text):
        words = text.split()
        return len(words)

    def count_characters(text):
        letters = "abcdefghijklmnopqrstuvwxyz"
        result = {}
        lower_text = text.lower()
        for letter in letters:
            result[letter] = lower_text.count(letter)
        return result

    def report(word_count, character_count):
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for letter, count in character_count.items():
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

    word_count = count_words(text)
    character_count = count_characters(text)
    report(word_count, character_count)

main()
