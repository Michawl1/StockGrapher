import seaborn as sns
import csv


def graph_spy():
    spy_data = None

    with open("../resources/US1.SPY15Min_DATA.csv") as spy:
        spy_data = csv.reader(spy, delimter=',')

    if spy_data is None:
        print("No spy back data found in resources")
        exit(1)

    ax = sns.boxplot(x="Time", y="price", data=spy_data)
