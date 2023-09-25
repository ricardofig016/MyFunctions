# I wrote this because someone asked me for words in portuguese that
# contain all the vowels. You can use this to search through the
# portuguese dictionary for words that have some characters and dont
# have others.


class WordSearch(object):
    def find_words(
        self,
        present_chrs: str,
        absent_chrs: str,
        min_size: int = 1,
        max_size: int = 1e10,
        file_path: str = "assets/portuguese_word_list.txt",
    ) -> list:
        word_list = []

        try:
            with open(file_path, "r", encoding="ISO-8859-1") as file:
                for line in file:
                    word = line.strip()
                    if word:  # To avoid adding empty lines
                        word_list.append(word)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return

        words = []
        for word in word_list:
            if len(word) < min_size or len(word) > max_size:
                continue
            valid = True
            for ch in present_chrs:
                if not ch in word:
                    valid = False
                    break
            for ch in absent_chrs:
                if ch in word:
                    valid = False
                    break
            if valid:
                words.append(word)

        return words


if __name__ == "__main__":
    s = WordSearch()
    words = s.find_words("aeiou", "-", 8, 8)
    print(words, "\n", len(words))
