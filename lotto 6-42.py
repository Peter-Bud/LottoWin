import csv


def main():
    temp_list = []
    all_data = []
    only_true = []


    with open('big_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            temp_list.append((', '.join(row)))


        for i in temp_list:
            new_int = int(i)
            all_data.append(new_int)

    super_ball = all_data[6::7]
    del all_data[6::7]
    print( all_data)


main()
