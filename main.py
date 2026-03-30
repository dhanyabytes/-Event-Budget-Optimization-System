# Event Budget Optimization System
# Author: Dhanya Thakur

def get_budget():
    while True:
        try:
            budget = float(input("Enter total event budget: "))
            if budget <= 0:
                print("Budget must be greater than 0.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_event_type():
    print("\nEvent Type:")
    print("1. Formal\n2. Informal\n3. Technical\n4. Cultural")
    choice = input("Enter choice: ")

    types = {"1": "formal", "2": "informal", "3": "technical", "4": "cultural"}
    return types.get(choice, "informal")


def get_priority():
    print("\nPriority Area:")
    print("1. Venue\n2. Food\n3. Marketing\n4. Logistics")
    choice = input("Enter choice: ")

    priorities = {"1": "venue", "2": "food", "3": "marketing", "4": "logistics"}
    return priorities.get(choice, "venue")


def allocate_budget(budget, event_type, priority):
    if event_type == "formal":
        allocation = {"venue": 0.4, "food": 0.3, "marketing": 0.1, "logistics": 0.2}
    elif event_type == "technical":
        allocation = {"venue": 0.3, "food": 0.2, "marketing": 0.2, "logistics": 0.3}
    elif event_type == "cultural":
        allocation = {"venue": 0.25, "food": 0.35, "marketing": 0.15, "logistics": 0.25}
    else:
        allocation = {"venue": 0.3, "food": 0.4, "marketing": 0.1, "logistics": 0.2}

    # Adjust priority
    for key in allocation:
        if key == priority:
            allocation[key] += 0.05
        else:
            allocation[key] -= 0.015

    # Normalize
    total = sum(allocation.values())
    for key in allocation:
        allocation[key] /= total

    return allocation


def display_result(budget, allocation):
    print("\n--- Optimized Budget ---")
    for k, v in allocation.items():
        print(f"{k.capitalize():<10}: ₹{budget * v:.2f} ({v*100:.1f}%)")


def main():
    print("=== Event Budget Optimization System ===")

    budget = get_budget()
    event_type = get_event_type()
    priority = get_priority()

    result = allocate_budget(budget, event_type, priority)
    display_result(budget, result)


if __name__ == "__main__":
    main()