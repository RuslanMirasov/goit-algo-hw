from itertools import count
from queue import Empty, Queue
from time import sleep

queue = Queue()
request_ids = count(1)


def generate_request():
    request = {"id": next(request_ids)}
    queue.put(request)
    print(f"Додано заявку #{request['id']}")


def process_request():
    try:
        request = queue.get_nowait()
    except Empty:
        print("Черга пуста")
        return

    print(f"Заявку #{request['id']} оброблено!")


def main():
    print("Сервіс запущено. Для виходу натисніть Ctrl + C\n")

    try:
        while True:
            generate_request()
            process_request()

            # Затримка в 1 секунду для зручностi перевiрки
            sleep(1)
    except KeyboardInterrupt:
        print("\nРоботу завершено.")


if __name__ == "__main__":
    main()
