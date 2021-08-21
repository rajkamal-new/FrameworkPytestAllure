import csv
import os



def read_csv_data(filename):

    parent_dir = os.getcwd()
    filepath = os.path.abspath(parent_dir+"/test_data/csv/"+filename)

    data = []
    with open(filepath) as file:
        obj = csv.reader(file)
        next(obj)
        for row in obj:
            data.append([row[i] for i in range(len(row))])
        return data



if __name__ == "__main__":
    print(get_csv_data("login_data.csv"))