import random
import timeit


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > current:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = current

    return numbers


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def generate_random_list(size):
    return [random.randint(0, 10000) for _ in range(size)]


def test_sorting(sort_function, numbers):
    return timeit.timeit(lambda: sort_function(numbers.copy()), number=1)


def print_result(size, insertion_time, merge_time, sorted_time):
    print(f"{size:<10}{insertion_time:<14f}{merge_time:<14f}{sorted_time:<14f}")


def main():
    random.seed(42)
    sizes = [100, 1000, 5000, 10000]

    print(f"{'Розмір':<10}{'Вставками':<14}{'Злиттям':<14}{'Timsort':<14}")
    print("-" * 46)

    for size in sizes:
        numbers = generate_random_list(size)

        insertion_time = test_sorting(insertion_sort, numbers)
        merge_time = test_sorting(merge_sort, numbers)
        sorted_time = test_sorting(sorted, numbers)

        print_result(size, insertion_time, merge_time, sorted_time)


if __name__ == "__main__":
    main()
