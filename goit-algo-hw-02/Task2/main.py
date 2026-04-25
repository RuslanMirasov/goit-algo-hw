from collections import deque


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    chars = deque(text)

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False

    return True


def main():
    print("Перевірка паліндрома. Для виходу натисніть Ctrl + C\n")

    try:
        while True:
            text = input("Введіть рядок: ")

            if is_palindrome(text):
                print("Це паліндром\n")
            else:
                print("Це не паліндром\n")
    except KeyboardInterrupt:
        print("\nРоботу завершено.")


if __name__ == "__main__":
    main()
