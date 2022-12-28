import matplotlib.pyplot as plt
import numpy as np
import random as rnd


def main():
    Coin = ["H", "T"]
    occurrences = []
    whole_occurrences = {}
    for i in range(100000):
        Count = 0
        for i in range(100):
            choice = rnd.choice(Coin)
            if choice == 'H':
                Count += 1
        occurrences.append(Count)
        if whole_occurrences.get(Count) == None:
            whole_occurrences[Count] = 1
        else:
            whole_occurrences[Count] += 1

    np_occurrences = np.array(occurrences)
    mean = np.mean(np_occurrences)
    median = np.median(np_occurrences)
    std = np.std(np_occurrences)
    print("mean: ", mean, "\nmedian: ", median, "\nstandard deviation: ", std)

    whole_occurrences_keys = list(whole_occurrences.keys())
    whole_occurrences_values = list(whole_occurrences.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(whole_occurrences_keys, whole_occurrences_values, color='purple')
    plt.plot(whole_occurrences_keys, whole_occurrences_values, linestyle='None')
    plt.title(
        "The probability of Heads when tossing a coin 100 times in 100,000 trials")
    plt.xlabel("Head percentage")
    plt.ylabel("Number of occurrences")
    plt.show()


main()
