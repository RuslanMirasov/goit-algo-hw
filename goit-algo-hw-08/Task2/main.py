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


def find_sum(root):
    if root is None:
        return 0

    return root.value + find_sum(root.left) + find_sum(root.right)


def create_tree(values):
    root = None

    for key in values:
        root = insert(root, key)

    return root


def main():
    values = [10, 5, 15, 89, 7, 12, 18]
    root = create_tree(values)
    total_sum = find_sum(root)

    print(f"Значення у дереві: {values}")
    print(f"Сума всіх значень у дереві: {total_sum}")


if __name__ == "__main__":
    main()
