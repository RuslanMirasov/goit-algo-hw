import argparse
import shutil
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="Копіює файли та сортує їх за розширеннями")
    parser.add_argument("source", type=Path, help="Шлях до вихідної папки")
    parser.add_argument("dist", nargs="?", type=Path, help="Папка призначення")

    return parser.parse_args()


def get_folder_name(file_path):
    return file_path.suffix.lower().lstrip(".") or "no_extension"


def get_new_file_path(file_path):
    counter = 1
    new_file_path = file_path

    while new_file_path.exists():
        new_file_path = file_path.with_name(f"{file_path.stem}_{counter}{file_path.suffix}")
        counter += 1

    return new_file_path


def copy_file(file_path, dist_path):
    folder_path = dist_path / get_folder_name(file_path)
    folder_path.mkdir(parents=True, exist_ok=True)

    new_file_path = get_new_file_path(folder_path / file_path.name)
    shutil.copy2(file_path, new_file_path)
    print(f"Скопійовано: {file_path} -> {new_file_path}")


def copy_files(source_path, dist_path):
    try:
        for item in source_path.iterdir():
            if item.resolve() == dist_path.resolve():
                continue

            if item.is_dir():
                copy_files(item, dist_path)
            elif item.is_file():
                copy_file(item, dist_path)
    except PermissionError:
        print(f"Немає доступу: {source_path}")
    except OSError as error:
        print(f"Помилка: {error}")


def main():
    args = parse_arguments()
    dist_path = args.dist or Path(__file__).parent / "dist"

    if not args.source.exists() or not args.source.is_dir():
        print("Вихідна папка не існує.")
        return

    dist_path.mkdir(parents=True, exist_ok=True)
    copy_files(args.source, dist_path)
    print("Роботу завершено.")


if __name__ == "__main__":
    main()
