import matplotlib.pyplot as plt
from load_csv import load


def format_data(data):
    """
    A function that format the data from the population_total.csv file
    to be able to plot it in a line graph.
    For each value in population, the function will transform the
    'XM' format to X * 10^6.

    Parameters:
        data (list): The data to format.
    """

    for i in range(len(data)):
        if data[i] == "NA":
            data[i] = 0
        else:
            data[i] = float(data[i][:-1]) * 10**6

    return data


def reduce_size(years, pop_france, pop_belgium):
    """
    A function that reduce the size of the data to have a max years at 2050
    Iterate over years until 2060 and cut the 2 pop list at the same size.
    """

    for i in range(len(years)):
        if int(years[i]) == 2050:
            years = years[:i+1]
            break

    length = len(years)
    pop_france = pop_france[:length]
    pop_belgium = pop_belgium[:length]

    return years, pop_france, pop_belgium


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
        fr_pop = format_data(france_population)
        belg_pop = format_data(belgium_population)

        years, fr_pop, belg_pop = reduce_size(years, fr_pop, belg_pop)

        plt.plot(years, fr_pop, label="France")
        plt.plot(years, belg_pop, label="Belgium")
        plt.xlabel("Years")
        plt.xticks(years[::40])
        plt.ylabel("Population")
        plt.yticks([20 * 10**6, 40 * 10**6, 60 * 10**6], ['20M', '40M', '60M'])
        plt.title("Population Projection")
        plt.legend()
        plt.legend(loc='lower right')
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
