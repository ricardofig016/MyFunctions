import unicodedata
from icecream import ic


def words(
    min_len=0,
    max_len=100,
    starts_with="",
    ends_with="",
    must_contain=[],
    cant_contain=[],
    case_sensitive=False,
    result_size=0,  # 0 is no max size
):
    with open("assets/portuguese_word_list.txt", "r", encoding="ISO-8859-1") as file:
        words = [line.strip() for line in file]

    result = []
    for word in words:
        if filter_word(
            word,
            min_len,
            max_len,
            starts_with,
            ends_with,
            must_contain,
            cant_contain,
            case_sensitive,
        ):
            result.append(word)
            if result_size and len(result) >= result_size:
                break

    return result


def filter_word(
    word,
    min_len=0,
    max_len=100,
    starts_with="",
    ends_with="",
    must_contain=[],
    cant_contain=[],
    case_sensitive=False,
):
    if not case_sensitive:
        word = word.lower()
        starts_with = starts_with.lower()
        ends_with = ends_with.lower()
        must_contain = [s.lower() for s in must_contain]
        cant_contain = [s.lower() for s in cant_contain]

    if len(word) < min_len or len(word) > max_len:
        return False

    if starts_with and word[: len(starts_with)] != starts_with:
        return False
    if ends_with and word[-len(ends_with) :] != ends_with:
        return False

    for exp in must_contain:
        if exp and exp.lower() not in word:
            return False
    for exp in cant_contain:
        if exp and exp.lower() in word:
            return False

    return True


if __name__ == "__main__":
    min_len = 0
    max_len = 10
    starts_with = "v"
    ends_with = "do"
    must_contain = ["n", "t"]
    cant_contain = ["-", "en"]
    case_sensitive = False
    result_size = 0

    result = words(
        min_len,
        max_len,
        starts_with,
        ends_with,
        must_contain,
        cant_contain,
        case_sensitive,
        result_size,
    )

    ic(result)
