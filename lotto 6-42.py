import requests
from bs4 import BeautifulSoup
import csv
from random import sample, choice

URL='https://igra.msl.ua/megalote/uk/archive'
HEADERS={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
         'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

def get_html(url, params=None):
    req=requests.get(url, headers=HEADERS, params=params)
    return req



def parse():
    html=get_html(URL)
    print(html)

parse()


def transform():
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
    return all_data, super_ball


def calculate():
    all_data, super_ball = transform()
    chance = []

    for i in range(0, 42):
        chance.append((all_data.count(i)) / len(all_data) * 100)
    average = sum(chance) / len(chance)
    min_list = []
    max_list = []

    for index, item in enumerate(chance):

        if item < average:
            min_list.append(index + 1)
        elif item >= average:
            max_list.append(index + 1)

    return min_list, max_list, super_ball


def result():
    min_list, max_list, super_ball = calculate()
    print('First attempt: ', sample(min_list, 6), 'Superball', '', choice(super_ball))
    print('The second attempt: ', sample(max_list, 6), 'Superball', '', choice(super_ball))


if __name__ == '__main__':
    result()
