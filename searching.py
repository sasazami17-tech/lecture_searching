from pathlib import Path
import json


def read_data(file_name, field):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        if field not in data:
            return None
        else:
            return data[field]
    except FileNotFoundError:
        return None

    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name



def main():
    nove_data = read_data("sequential.json", "unordered_numbers")
    print(nove_data)

def linear_search(sekvencia, hladane_heslo):
    miesto = [] #1

    for i in range(len(sekvencia)): # n
        if sekvencia[i] == hladane_heslo: # n
            miesto.append(i)# 0

    return {"positions": miesto, "count": len(miesto)} # 1
#najhorise = 3n + 2 = O(n(
def main():
    data = read_data("sequential.json", "unordered_numbers")
    miesto = 5

    vysledok = linear_search(data, miesto)
    print(vysledok)

if __name__ == "__main__":
    main()

def binary_search(seznam_cisel, hladane_cislo):
    lave = 0
    prave = len(seznam_cisel) - 1

    while lave <= prave:
        stred = (lave + prave) // 2

        if seznam_cisel[stred] == hladane_cislo:
            return stred
        elif seznam_cisel[stred] < hladane_cislo:
            lave = stred + 1
        else:
            prave = stred - 1

    return None

def main():
    data = read_data("sequential.json", "ordered_numbers")
    hladane_cislo = 45

    vysledok = binary_search(data, hladane_cislo)
    print(vysledok)

# import time
#
# numbers = [4, 8, 15, 16, 23, 42, 55, 78, 91, 120]
# target = 78
#
# start = time.perf_counter()
#
# for number in numbers:
#     if number == target:
#         break
#
# end = time.perf_counter()
#
# duration = end - start
# print(f"Měření trvalo {duration:.8f} s")

from generators import unordered_sequence
import random
import time
import matplotlib.pyplot as plt


# 🔍 Sekvenční vyhledávání
def sequential_search(data, target):
    for vec in data:
        if vec == target:
            return True
    return False



def binary_search(data, hladane_cislo):
    lave = 0
    prave = len(data) - 1

    while lave <= prave:
        stred = (lave + prave) // 2

        if data[stred] == hladane_cislo:
            return True
        elif data[stred] < hladane_cislo:
            lave = stred + 1
        else:
            prave = stred - 1

    return False



def measure_time(f, data, hladane_cislo, opakuj=10):
    cas = 0

    for _ in range(opakuj):
        start = time.perf_counter()
        f(data, hladane_cislo)
        koniec = time.perf_counter()
        cas += (koniec - start)

    return cas / opakuj


def main():
    velkosti = [100, 500, 1000, 5000, 10000]

    sequential_times = []
    binary_times = []
    set_times = []

    for velkost in velkosti:

        data = unordered_sequence(velkost)
        hladane_cislo = random.choice(data)


        s_cas = measure_time(sequential_search, data, hladane_cislo)
        sequential_times.append(s_cas)

        sorted_data = sorted(data)
        bin_cas = measure_time(binary_search, sorted_data, hladane_cislo)
        binary_times.append(bin_cas)


        data_set = set(data)
        set_time = measure_time(lambda d, t: t in d, data_set, hladane_cislo)
        set_times.append(set_time)

    plt.figure(figsize=(8, 5))

    plt.plot(velkosti, sequential_times, label="Sekvencni vyhledavani")
    plt.plot(velkosti, binary_times, label="Binarni vyhledavani")
    plt.plot(velkosti, set_times, label="Set (mnozina)")

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Cas (s)")
    plt.title("Porovnani algoritmu vyhledavani")

    plt.legend()
    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()

