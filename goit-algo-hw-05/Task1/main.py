import timeit
from pathlib import Path

from boyer_moore_algorithm import boyer_moore_search
from knuth_morris_pratt_algorithm import kmp_search
from rabin_karp_algorithm import rabin_karp_search


RUNS_COUNT = 100


def read_text(file_name):
    file_path = Path(__file__).parent / file_name

    for encoding in ("utf-8", "cp1251"):
        try:
            return file_path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue

    return file_path.read_text(encoding="utf-8", errors="ignore")


def measure_search_time(search_function, text, pattern):
    total_time = timeit.timeit(lambda: search_function(text, pattern), number=RUNS_COUNT)
    return total_time / RUNS_COUNT


def print_result(text_name, pattern_type, algorithm_name, search_time, position):
    print(
        f"{text_name:<8}"
        f"{pattern_type:<14}"
        f"{algorithm_name:<26}"
        f"{search_time:<12.6f}"
        f"{position:<8}"
    )


def main():
    texts = {
        "text1": read_text("text1.txt"),
        "text2": read_text("text2.txt"),
    }

    patterns = {
        "існуючий": "структури даних",
        "вигаданий": "вигаданий фрагмент, якого точно немає у статтях",
    }

    search_algorithms = {
        "Boyer-Moore": boyer_moore_search,
        "Knuth-Morris-Pratt": kmp_search,
        "Rabin-Karp": rabin_karp_search,
    }

    print(f"{'Текст':<8}{'Підрядок':<14}{'Алгоритм':<26}{'Сер. час':<12}{'Індекс':<8}")
    print("-" * 68)

    for text_name, text in texts.items():
        for pattern_type, pattern in patterns.items():
            for algorithm_name, search_function in search_algorithms.items():
                search_time = measure_search_time(search_function, text, pattern)
                position = search_function(text, pattern)
                print_result(text_name, pattern_type, algorithm_name, search_time, position)


if __name__ == "__main__":
    main()
