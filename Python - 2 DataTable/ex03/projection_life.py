import matplotlib.pyplot as plt
from load_csv import load


def select_good_year(life_data, income_data):
    """
    Iterate over all the data in the life_data and income_data
    and select the data for the year 1900.
    That slice each data to only have the data for the year 1900
    and the name of the country.
    The year 1900 is the 101th value in the data.
    """

    life_1900 = life_data.iloc[:, [0, 101]]
    life_1900.columns = ["country", "life_expectancy"]
    income_1900 = income_data.iloc[:, [0, 101]]
    income_1900.columns = ["country", "income"]

    return life_1900, income_1900


def main():
    """
    A program that load the data from the 2 csv files in current folder
    with the load function in load_csv. It then display a projection of
    life expectancy in relation to the gross national product of the year 1900
    for each country in the data.
    """

    try:
        life_data = load("life_expectancy_years.csv")
        income_data = load("income_per_person_gdppercapita_ppp.csv")

        life_1900, income_1900 = select_good_year(life_data, income_data)

        plt.figure(figsize=(8, 6))
        plt.plot(income_1900["income"], life_1900["life_expectancy"], "ob")
        plt.xlabel("Gross Domestic Product")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.tight_layout()
        plt.show()

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
