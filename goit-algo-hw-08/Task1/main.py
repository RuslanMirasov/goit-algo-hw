class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def find_min(root):
    if root is None:
        return None

    current = root

    while current.left is not None:
        current = current.left

    return current.value


def create_tree(values):
    root = None

    for key in values:
        root = insert(root, key)

    return root


def main():
    values = [10, 5, 15, 89, 7, 12, 18]
    root = create_tree(values)
    min_value = find_min(root)

    print(f"Значення у дереві: {values}")
    print(f"Найменше значення у дереві: {min_value}")


if __name__ == "__main__":
    main()
