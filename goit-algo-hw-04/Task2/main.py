import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
        return

    for angle in [60, -120, 60, 0]:
        koch_curve(t, order - 1, size / 3)
        t.left(angle)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("black")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.color("white")
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    koch_snowflake(t, order, size)

    window.mainloop()


def get_order():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

            if order < 0:
                print("Рівень рекурсії має бути невід'ємним числом.")
                continue

            return order
        except ValueError:
            print("Помилка! Введіть ціле число.")


def main():
    order = get_order()
    draw_koch_snowflake(order)


if __name__ == "__main__":
    main()
