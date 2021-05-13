import csv


def graph_stock(csv_path):
    """

    :param csv_path: a path to a csv file that contains stock back data.
                     data shall be formatted as a csv with the columns:
                     <TICKER>,<PER>,<DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>

    :return:
    """

    with open(csv_path) as stock:
        stock = csv.reader(stock, delimiter=',')

        for line in stock:
            print(line)
