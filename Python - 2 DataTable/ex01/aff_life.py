import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    A program that load the data from the .csv file
    with the load function in load_csv. It then
    choose the data from France Country and display it in a line graph.
    """
    try:
        data = load("life_expectancy_years.csv")
        france_data = data[data["country"] == "France"]
        years = france_data.columns[1:]
        life_expectancy = france_data.values[0][1:]

        plt.plot(years, life_expectancy)
        plt.xlabel("Years")
        plt.xticks(years[::40])
        plt.ylabel("Life Expectancy")
        plt.title("France Life Expectancy Projection")
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
