import csv


def main():
    temp_list = []
    all_data = []



    with open('big_data.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        for row in spamreader:
            temp_list.append((', '.join(row)))


        for i in temp_list:
            new_int = int(i)
            all_data.append(new_int)

    super_ball = all_data[6::7]
    del all_data[6::7]
    chance = []

    for i in range(0,42):
        chance.append((all_data.count(i))/len(all_data)*100)



    average= sum(chance)/len(chance)
    min_list=[]
    max_list=[]
    for index, item in enumerate(chance):

        if item<average:
            print(index+1,item)
            min_list.append(index+1)
        elif item>=average:
            max_list.append(index+1)

    print(max_list)
    print(min_list)






main()








