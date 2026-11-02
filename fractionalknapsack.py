
# Fractional Knapsack using Greedy Algorithm

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight


items = []

while True:
    print("\n=== Fractional Knapsack Menu ===")
    print("1. Enter items")
    print("2. Solve fractional knapsack")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        items.clear()

        n = int(input("Enter number of items: "))

        for i in range(n):
            print("Item", i + 1, "value:")
            v = int(input())

            print("Item", i + 1, "weight:")
            w = int(input())

            if w <= 0:
                print("Weight must be positive!")
                continue

            items.append(Item(v, w))

    elif choice == 2:

        if not items:
            print("Please enter items first!")
            continue

        capacity = int(input("Enter knapsack capacity: "))

        if capacity < 0:
            print("Capacity cannot be negative!")
            continue

        # Sort items by value-to-weight ratio
        items.sort(key=lambda x: x.ratio, reverse=True)

        total_value = 0
        remaining = capacity

        print("\nItems taken (value/weight fraction):")

        for item in items:

            if remaining == 0:
                break

            if item.weight <= remaining:
                print(item.value, "/", item.weight, "-> Full")

                total_value += item.value
                remaining -= item.weight

            else:
                fraction = remaining / item.weight

                print(item.value, "/", item.weight,
                      "->", fraction * 100, "%")

                total_value += item.value * fraction
                remaining = 0

        print("Maximum total value in knapsack: {:.2f}".format(total_value))

    elif choice == 3:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice!")
