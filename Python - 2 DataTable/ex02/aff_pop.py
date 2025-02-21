import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    A program that load the data from the population_total.csv file
    with the load function in load_csv. It then choose the data from
    France Country and display it in a line graph in comparaison with
    the Belgium population.
    """

    try:
        data = load("population_total.csv")
        france_data = data[data["country"] == "France"]
        belgium_data = data[data["country"] == "Belgium"]
        years = france_data.columns[1:]
        france_population = france_data.values[0][1:]
        belgium_population = belgium_data.values[0][1:]

        print(f"france_population: {france_population}")
        print(f"belgium_population: {belgium_population}")

        plt.plot(years, france_population, label="France")
        plt.plot(years, belgium_population, label="Belgium")
        plt.xlabel("Years")
        plt.xticks(years[::40])
        plt.ylabel("Population")
        plt.yticks(range(20, 101, 20))
        plt.title("Population Projection")
        plt.legend()
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()