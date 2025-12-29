import matplotlib.pyplot as plt

def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), 
        key=lambda x: x[1]["calories"] / x[1]["cost"], 
        reverse=True
    )

    selected_items = []
    total_calories = 0
    remaining_budget = budget

    for name, data in sorted_items:
        if data["cost"] <= remaining_budget:
            selected_items.append(name)
            total_calories += data["calories"]
            remaining_budget -= data["cost"]

    return {
        "items": selected_items,
        "total_calories": total_calories,
        "remaining_budget": remaining_budget
    }

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            if costs[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - costs[i-1]] + calories[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(names[i-1])
            w -= costs[i-1]

    return {
        "items": selected_items,
        "total_calories": dp[n][budget],
        "remaining_budget": w
    }

def visualize_comparison(items, budget):
    greedy_res = greedy_algorithm(items, budget)
    dp_res = dynamic_programming(items, budget)
    methods = ['Жадібний', 'Динамічний']
    calories = [greedy_res['total_calories'], dp_res['total_calories']]

    plt.figure(figsize=(14, 7))

    # --- ЛІВИЙ ГРАФІК: Сумарна калорійність ---
    plt.subplot(1, 2, 1)
    bars = plt.bar(methods, calories, color=['skyblue', 'salmon'])
    plt.title(f'Сумарна калорійність на бюджет у {budget}₴', fontsize=12)
    plt.ylabel('Загальні калорії')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 5, f"{int(yval)} ккал", ha='center', va='bottom', fontweight='bold')

    # --- ПРАВИЙ ГРАФІК: Вибір страв ---
    plt.subplot(1, 2, 2)

    labels_with_data = [
        f"{name}\n({data['cost']}₴, {data['calories']} ккал)" 
        for name, data in items.items()
    ]
    
    all_food_keys = list(items.keys())
    greedy_selection = [1 if food in greedy_res['items'] else 0 for food in all_food_keys]
    dp_selection = [1 if food in dp_res['items'] else 0 for food in all_food_keys]
    
    x = range(len(all_food_keys))
    width = 0.35

    plt.bar([p - width/2 for p in x], greedy_selection, width, label='Жадібний', color='skyblue', alpha=0.8)
    plt.bar([p + width/2 for p in x], dp_selection, width, label='Динамічний', color='salmon', alpha=0.8)

    plt.title('Деталі вибору страв', fontsize=12)
    plt.xticks(x, labels_with_data, rotation=45, ha='right', fontsize=9)
    plt.yticks([0, 1], ['Не обрано', 'Обрано'])
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.show()

# Приклад використання:
budget = 100
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

print(f"\n--- Бюджет: {budget}₴ ---")

greedy_res = greedy_algorithm(items, budget)
print("\nЖадібний алгоритм (пріоритет за співвідношенням калорії/вартість):")
print(f"Страви: {greedy_res['items']}")
print(f"Загальна калорійність: {greedy_res['total_calories']}")
print(f"Залишок бюджету: {greedy_res['remaining_budget']}")

dp_res = dynamic_programming(items, budget)
print("\nДинамічне програмування (пошук глобального оптимуму):")
print(f"Страви: {dp_res['items']}")
print(f"Загальна калорійність: {dp_res['total_calories']}")
print(f"Залишок бюджету: {dp_res['remaining_budget']}")

visualize_comparison(items, budget)
