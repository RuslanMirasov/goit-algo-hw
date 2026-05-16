import heapq


def find_min_cost(cables):
    if not cables:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second

        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost


def main():
    cables = [4, 3, 2, 6]
    min_cost = find_min_cost(cables.copy())

    print(f"Довжини кабелів: {cables}")
    print(f"Мінімальні витрати на об'єднання: {min_cost}")


if __name__ == "__main__":
    main()
