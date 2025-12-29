import random
import pandas
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_throws=100000):
    sums_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_throws):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_counts[total] += 1

    probabilities = {s: (count / num_throws) * 100 for s, count in sums_counts.items()}
    return probabilities

def simulate_dice_rolls_comparison():
    num_throws = 100000
    mc_probs = monte_carlo_simulation(num_throws)

    analytical_probs = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    df = pandas.DataFrame({
        'Сума': list(mc_probs.keys()),
        'Монте-Карло (%)': [round(mc_probs[s], 2) for s in mc_probs],
        'Аналітична (%)': [analytical_probs[s] for s in analytical_probs]
    })

    df['Різниця (%)'] = abs(df['Монте-Карло (%)'] - df['Аналітична (%)']).round(2)

    print(f"Результати симуляції ({num_throws} кидків):")
    print(df.to_string(index=False))

    plt.figure(figsize=(10, 6))
    plt.bar(df['Сума'] - 0.2, df['Монте-Карло (%)'], width=0.4, label='Монте-Карло', color='skyblue')
    plt.bar(df['Сума'] + 0.2, df['Аналітична (%)'], width=0.4, label='Аналітична', color='salmon', alpha=0.7)

    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння методу Монте-Карло та аналітичних розрахунків')
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    simulate_dice_rolls_comparison()
