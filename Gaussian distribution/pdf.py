import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def pdf(occurrences, mean, std):
    y = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (occurrences - mean)**2 / (2 * std**2))
    return y

def main():  
    Coin = ["H", "T"]
    occurrences = []
    for i in range(100000):
        Count = 0
        for i in range(100):
            choice = rnd.choice(Coin)
            if choice == 'H':
                Count += 1
        occurrences.append(Count)

    np_occurrences = np.array(occurrences)
    mean = np.mean(np_occurrences)
    median = np.median(np_occurrences)
    std = np.std(np_occurrences)
    y = pdf(np_occurrences, mean, std)
    print("mean: ",mean,"\nmedian: ", median, "\nstandard deviation: ",std)
    plt.figure(figsize = (10, 6))
    plt.scatter( occurrences, y, marker = 'o', s = 25, color = 'purple')
    plt.plot(occurrences, y, color = 'black', linestyle = 'None')
    plt.title(
        "The probability of Heads when tossing a coin 100 times in 100,000 trials")
    plt.xlabel("Head percentage")
    plt.ylabel("PDF")
    plt.show()

main()